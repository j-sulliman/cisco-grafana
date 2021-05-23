import requests
import time
import pprint as pp
from requests.auth import HTTPBasicAuth
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)

import os
import sys

# Add your own path to django install location here
sys.path.append("/Users/jamespsullivan/Documents/grafana-cisco-demo/cisco_grafana/")

# We need to import django configuration settings to write our API response using the django models API
os.environ['DJANGO_SETTINGS_MODULE'] = 'cisco_grafana.settings'

import django
django.setup()
from sdwan.models import sdwan_devices, sdwan_deviceCounters

def get_jsessionid(vmanage_host, vmanage_port, username, password):
        api = "/j_security_check"
        base_url = "https://{}:{}".format(vmanage_host, vmanage_port)
        url = base_url + api
        payload = {'j_username' : username, 'j_password' : password}

        response = requests.post(url=url, data=payload, verify=False)
        try:
            cookies = response.headers["Set-Cookie"]
            jsessionid = cookies.split(";")
            return(jsessionid[0])
        except:
            if logger is not None:
                logger.error("No valid JSESSION ID returned\n")
            exit()


def get_token(vmanage_host, vmanage_port, jsessionid):
    headers = {'Cookie': jsessionid}
    base_url = "https://{}:{}".format(vmanage_host, vmanage_port)
    api = "/dataservice/client/token"
    url = base_url + api
    response = requests.get(url=url, headers=headers, verify=False)
    if response.status_code == 200:
        return(response.text)
    else:
        return None


def vmanage_get(token, jsessionid, vmanage_host='192.168.200.42',
    vmanage_port='443', querystring = '/devices'):
    # Pass our token and session-id to header used in requests query
    if token is not None:
        header = {'Content-Type': "application/json",'Cookie': jsessionid,
            'X-XSRF-TOKEN': token}
    else:
        header = {'Content-Type': "application/json",'Cookie': jsessionid}
    # The vamanage API
    base_url = "https://{}:{}/dataservice".format(vmanage_host, vmanage_port)
    url = base_url + querystring
    # Pass the token and session ID to request headers
    response = requests.get(url=url, headers=header,verify=False)
    # Check that the request was successful
    if response.status_code == 200:
        try:
            items = response.json()['data']
        except KeyError:
            print('Data key does not exist')
            items = response.json()
        except TypeError:
            print('Type Error')
            print(response)
    elif response.status_code != 200:
        print('API Call Failed - received status code {}'.format(
            response.status_code))
        items = 'API Call Failed - received status code {}'.format(
            response.status_code)
    return items

def devices_to_db(devices):
    for device in devices:
        if device['device-type'] == 'vmanage' or device['device-type'] == 'vsmart':
            sdwan_device = sdwan_devices(
            deviceId = device['deviceId'],
            system_ip = device['system-ip'],
            host_name = device['host-name'],
            reachability = device['reachability'],
            status = device['status'],
            personality = device['personality'],
            device_type = device['device-type'],
            lastupdated = device['lastupdated'],
            domain_id = device['domain-id'],
            board_serial = device['board-serial'],
            certificate_validity = device['certificate-validity'],
            site_id = device['site-id'],
            latitude = device['latitude'],
            longitude = device['longitude'],
            uptime_date = device['uptime-date'],
            validity = device['validity'],
            state = device['state'],
            state_description = device['state_description'],
            local_system_ip = device['local-system-ip'],
            version = device['version']
            )
            sdwan_device.save()
        elif device['device-type'] == 'vedge':
            sdwan_device = sdwan_devices(
            deviceId = device['deviceId'],
            system_ip = device['system-ip'],
            host_name = device['host-name'],
            reachability = device['reachability'],
            status = device['status'],
            personality = device['personality'],
            device_type = device['device-type'],
            lastupdated = device['lastupdated'],
            domain_id = device['domain-id'],
            board_serial = device['board-serial'],
            certificate_validity = device['certificate-validity'],
            site_id = device['site-id'],
            latitude = device['latitude'],
            longitude = device['longitude'],
            uptime_date = device['uptime-date'],
            validity = device['validity'],
            state = device['state'],
            state_description = device['state_description'],
            local_system_ip = device['local-system-ip'],
            version = device['version']
            )
            sdwan_device.save()


def device_counter_to_db(device_counters):
    for counter in device_counters:
        if 'bfdSessionsUp' in counter:
            device_counter = sdwan_deviceCounters(
            crashCount = counter['crashCount'],
            expectedControlConnections = counter['expectedControlConnections'],
            number_vsmart_control_connections = counter['number-vsmart-control-connections'],
            rebootCount = counter['rebootCount'],
            systemIp = counter['system-ip'],
            bfdSessionsUp = counter['bfdSessionsUp'],
            bfdSessionsDown = counter['bfdSessionsDown'],
            ompPeersDown = counter['ompPeersDown'],
            ompPeersUp = counter['ompPeersUp']
            )
            device_counter.save()


session_id = get_jsessionid(vmanage_host='192.168.200.42',
                vmanage_port='443',
                username='admin',
                password='Cisco123!')

token = get_token(vmanage_host='192.168.200.42',
            vmanage_port='443',
            jsessionid=session_id)

devices = vmanage_get(token, session_id, vmanage_host='192.168.200.42',
                        vmanage_port='443',
                        querystring='/device'
                        )
devices_to_db(devices)
device_counters = vmanage_get(token, session_id, vmanage_host='192.168.200.42',
                        vmanage_port='443',
                        querystring='/device/counters'
                        )
device_counter_to_db(device_counters)

for i in sdwan_deviceCounters.objects.all():
    print('-------------')
    print(i)
    print(i.bfdSessionsUp)
