import os
import time
import datetime
from django.utils import timezone
from django.core.mail import send_mail
import requests
from requests.auth import HTTPBasicAuth
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)

# Add your own path to django install location here
import sys
sys.path.append("/Users/jamespsullivan/Documents/grafana-cisco-demo/cisco_grafana/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'cisco_grafana.settings'

import django
import json

import pprint as pp
django.setup()

from openvuln.models import openvuln_advisory
from dcnm.models import dcnm_network_switch
from sdwan.models import sdwan_devices

def get_oauth_token(client_id, client_secret, request_token_url="https://cloudsso.cisco.com/as/token.oauth2"):
    """Get OAuth2 token from api based on client id and secret.
    :param client_id: Client id stored in config file.
    :param client_secret: Client secret stored in config file.
    :param request_token_url: the POST URL to request a token response
    :return The valid access token to pass to api in header.
    :raise requests exhibits anything other than a 200 response.
    """

    r = requests.post(
        request_token_url if request_token_url else REQUEST_TOKEN_URL,
        params={'client_id': client_id, 'client_secret': client_secret},
        data={'grant_type': 'client_credentials'}
    )
    return r.json()['access_token']

MIME_TYPE = 'application/json'
def rest_with_auth_headers(auth_token, user_agent):
    """Construct per session for sending with all GET requests to API."""
    return {
        'Authorization': 'Bearer {}'.format(auth_token),
        'Accept': MIME_TYPE,
        'User-Agent': user_agent,
    }


def openvuln_http_get(url='https://api.cisco.com/security/advisories/latest/100'):
    CLIENT_ID = "gh2q5unf7efe2evppgejjrpp"
    CLIENT_SECRET = "gZQGFK6S9NtyemzXQv4bNDTP"
    API_URL = "https://api.cisco.com/security/advisories"
    token = get_oauth_token(client_id=CLIENT_ID, client_secret=CLIENT_SECRET) # Get a Token
    header = {
        'Authorization': 'Bearer {}'.format(token),
        'Accept': 'application/json',
        'User-Agent': 'openvuln_api',
    }
    url = url #Network Device endpoint
    querystring = ''
    resp = requests.get(url, headers=header, verify=False)  # Make the Get Request
    advisories = resp.json() # Capture data from the controller

    return advisories, resp.status_code


def advisories_to_db(advisories):
    for advisory in advisories['advisories']:
        if advisory['cvssBaseScore'] == 'NA':
            advisory['cvssBaseScore'] = '0'
        advisory_update = openvuln_advisory(
            advisoryId = advisory['advisoryId'],
            advisoryTitle = advisory['advisoryTitle'],
            bugIDs = advisory['bugIDs'],
            cves = advisory['cves'],
            cvrfUrl = advisory['cvrfUrl'],
            cvssBaseScore = float(advisory['cvssBaseScore']),
            cwe = advisory['cwe'],
            firstPublished = advisory['firstPublished'],
            ipsSignatures = advisory['ipsSignatures'],
            lastUpdated = advisory['lastUpdated'],
            productNames = advisory['productNames'],
            publicationUrl = advisory['publicationUrl'],
            sir = advisory['sir'],
            status = advisory['status'],
            summary = advisory['summary']
        )
        advisory_update.save()

token = get_oauth_token(client_id='gh2q5unf7efe2evppgejjrpp',
                        client_secret='gZQGFK6S9NtyemzXQv4bNDTP')

psirts, status = openvuln_http_get()

advisories_to_db(psirts)


for psirt in openvuln_advisory.objects.all():
    if 'NX-OS' in psirt.productNames:
        psirt.devicesImpacted = 'NX-OS'
        psirt.save()
    elif 'SD-WAN' in psirt.productNames:
        psirt.devicesImpacted = 'SD-WAN'
        psirt.save()
    elif 'IOS' in psirt.productNames:
        psirt.devicesImpacted = 'IOS XE/IOS'
        psirt.save()
    elif 'Firepower' in psirt.productNames:
        psirt.devicesImpacted = 'ASA/Firepower'
        psirt.save()
    elif 'Unified Communications' in psirt.productNames:
        psirt.devicesImpacted = 'Collab'
        psirt.save()
    elif 'Jabber' in psirt.productNames:
        psirt.devicesImpacted = 'Collab'
        psirt.save()
    elif 'Webex' in psirt.productNames:
        psirt.devicesImpacted = 'Collab'
        psirt.save()
    elif 'HyperFlex' in psirt.productNames:
        psirt.devicesImpacted = 'Hyperflex'
        psirt.save()
    else:
        psirt.devicesImpacted = 'other'
        psirt.save()



    #print('ID: {}, Title: {}').format(psirt.advisoryId, psirt.advisoryTitle)
