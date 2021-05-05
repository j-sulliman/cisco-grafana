
import requests
import time
import pprint as pp
from requests.auth import HTTPBasicAuth
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)


DCNM_USER = "admin"
DCNM_PASSWORD = "Cisco123!"
dcnm = '192.168.200.230'

def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = 'https://{}/rest/logon'.format(dcnm)       # Endpoint URL
    data= '{"expirationTime": 360000}'
    resp = requests.post(url, auth=HTTPBasicAuth(DCNM_USER, DCNM_PASSWORD), verify=False, data=data)  # Make the POST Request
    token = resp.json()['Dcnm-Token']    # Retrieve the Token from the returned JSON
    print("Token Retrieved: {}".format(token))  # Print out the Token
    return token    # Create a return statement to send the token back for later use


def dcnm_http_get(dcnm_class):
    token = get_auth_token() # Get a Token
    url = url = 'https://{}/rest{}'.format(dcnm, dcnm_class)  #Network Device endpoint
    payload = {}
    hdr = {'Dcnm-Token': token, 'content-type' : 'application/json'}
    querystring = ''

    resp = requests.get(url, headers=hdr, verify=False, data=payload)  # Make the Get Request
    device_list = resp.json() # Capture data from the controller
    pp.pprint(device_list)
    return device_list # Pretty print the data

dcnm_http_get('/inventory/switches')
dcnm_http_get('/control/fabrics')
