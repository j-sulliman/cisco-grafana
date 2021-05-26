
import os
import time
import datetime
from django.utils import timezone
from django.core.mail import send_mail
import requests
from requests.auth import HTTPBasicAuth
import pprint as pp
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)

# Add your own path to django install location here
import sys
sys.path.append("/home/jamie/Documents/cicsco_grafana")
os.environ['DJANGO_SETTINGS_MODULE'] = 'cisco_grafana.settings'
import django
django.setup()

#from dnac.models import dnac_network_device, dnac_site_health, dnac_issues

def get_auth_token(DNAC_USER='devnetuser', DNAC_PASSWORD='Cisco123!',
                    dnac='sandboxdnac.cisco.com'):
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = 'https://{}/dna/system/api/v1/auth/token'.format(dnac)       # Endpoint URL
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD))  # Make the POST Request
    token = resp.json()['Token']    # Retrieve the Token from the returned JSON
    return token    # Create a return statement to send the token back for later use


def dnac_http_get(dnac_class):
    token = get_auth_token() # Get a Token
    url = "https://sandboxdnac.cisco.com/{}".format(dnac_class) #Network Device endpoint
    hdr = {'x-auth-token': token, 'content-type' : 'application/json'} #Build header Info
    #querystring = {"macAddress":"00:c8:8b:80:bb:00","managementIpAddress":"10.10.22.74"}
    querystring = ''

    resp = requests.get(url, headers=hdr, params=querystring)  # Make the Get Request
    device_list = resp.json() # Capture data from the controller
    return device_list # Pretty print the data

devices = dnac_http_get(dnac_class = 'api/v1/network-device')
issues = dnac_http_get(dnac_class='dna/intent/api/v1/issues')
events = dnac_http_get(dnac_class='dna/intent/api/v1/events')
vlans = dnac_http_get(dnac_class='dna/intent/api/v1/AssuranceGetSensorTestResults')
pp.pprint(vlans)
