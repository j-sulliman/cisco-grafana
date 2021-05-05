
import requests
import time
import pprint as pp
from requests.auth import HTTPBasicAuth
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)

def meraki_http_get(meraki_url):
    base_url = ('https://api.meraki.com/api/v1/{}'.format(meraki_url))

    headers = {'X-Cisco-Meraki-API-Key': '364db71a8327f27e0178fca518867f6038d58609'}
    try:
        get_response = requests.get(base_url, headers=headers, verify=False)
        status = get_response.status_code
        get_response = get_response.json()
        time.sleep(0.5)
    except:
        print('Meraki Cloud not reachable - check connection')
        get_response = 'unreachable'
        status = get_response.status_code
    return get_response, status


org_resp, api_status = meraki_http_get(meraki_url='organizations')
print(org_resp)
pp.pprint(org_resp)


import os
import sys

# Add your own path to django install location here
sys.path.append("/Users/jamespsullivan/Documents/grafana-cisco-demo/cisco_grafana/")

# We need to import django configuration settings to write our API response using the django models API
os.environ['DJANGO_SETTINGS_MODULE'] = 'cisco_grafana.settings'

import django
django.setup()

# Import the model we defined earlier
from meraki.models import Organizations, MerakiNetworks, MerakiDevices

# Write function to iterate over organisations found in our API request and save these to database
def meraki_orgs_to_db(data):
    for org in data:
        org_entry = Organizations(
            id = org['id'],
            name = org['name'],
            url = org['url']
            )
        org_entry.save()

# Call function and pass in our organisation data from api response
meraki_orgs_to_db(org_resp)

def meraki_networks_to_db():
    for orgs in Organizations.objects.all():
        networks, status = meraki_http_get('organizations/{}/networks'.format(
                        orgs.id))
        for network in networks:
            pp.pprint(network)
            network_entry = MerakiNetworks(
                id = network['id'],
                name = network['name'],
                organizationId = network['organizationId'],
                productTypes = network['productTypes'],
                timeZone = network['timeZone']
                )
            network_entry.save()

meraki_networks_to_db()

def meraki_devices_to_db():
    for networks in MerakiNetworks.objects.all():
        devices, status = meraki_http_get('networks/{}/devices'.format(
                        networks.id))
        for device in devices:
            if 'MX' in device['model']:
                device_entry = MerakiDevices(
                    address = device['address'],
                    serial = device['serial'],
                    mac = device['mac'],
                    lanIp = 'NA',
                    url = device['url'],
                    networkId = device['networkId'],
                    firmware = device['firmware'],
                    model = device['model'],
                    wan1Ip = device['wan1Ip'],
                    wan2Ip = device['wan2Ip']
                    )
                device_entry.save()
            elif 'MX' not in device['model']:
                device_entry = MerakiDevices(
                    address = device['address'],
                    serial = device['serial'],
                    firmware = device['firmware'],
                    mac = device['mac'],
                    lanIp = device['lanIp'],
                    url = device['url'],
                    networkId = device['networkId'],
                    model = device['model']
                    )
                device_entry.save()


meraki_devices_to_db()
