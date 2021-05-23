
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
from dcnm.models import dcnm_network_device, dcnm_network_switch

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


def get_dcnm_network_device(query_class):
            try:
                devices = dcnm_http_get(query_class)
                for device in devices:
                    if device['fabricType'] == 'Switch_Fabric':
                        device_entry=dcnm_network_device(
                            dcnm_addr = dcnm,
                            asn = device['asn'],
                            deviceType = device['deviceType'],
                            fabricId = device['fabricId'],
                            fabricName = device['fabricName'],
                            fabricTechnology = device['fabricTechnology'],
                            fabricType = device['fabricType'],
                            id = device['id'],
                            networkTemplate = device['networkTemplate'],
                            ADVERTISE_PIP_BGP = device['nvPairs']['ADVERTISE_PIP_BGP'],
                            ANYCAST_GW_MAC = device['nvPairs']['ANYCAST_GW_MAC'],
                            ANYCAST_RP_IP_RANGE = device['nvPairs']['ANYCAST_RP_IP_RANGE'],
                            BFD_ENABLE = device['nvPairs']['BFD_ENABLE'],
                            BFD_AUTH_ENABLE = device['nvPairs']['BFD_AUTH_ENABLE'],
                            BGP_AS = device['nvPairs']['BGP_AS'],
                            BGP_AUTH_ENABLE = device['nvPairs']['BGP_AUTH_ENABLE'],
                            DCI_SUBNET_RANGE = device['nvPairs']['DCI_SUBNET_RANGE'],
                            DCI_SUBNET_TARGET_MASK = device['nvPairs']['DCI_SUBNET_TARGET_MASK'],
                            DHCP_ENABLE = device['nvPairs']['DHCP_ENABLE'],
                            ENABLE_EVPN = device['nvPairs']['ENABLE_EVPN'],
                            ENABLE_NXAPI = device['nvPairs']['ENABLE_NXAPI'],
                            FABRIC_INTERFACE_TYPE = device['nvPairs']['FABRIC_INTERFACE_TYPE'],
                            FABRIC_MTU = device['nvPairs']['FABRIC_MTU'],
                            FABRIC_NAME = device['nvPairs']['FABRIC_NAME'],
                            L2_SEGMENT_ID_RANGE = device['nvPairs']['L2_SEGMENT_ID_RANGE'],
                            L3_PARTITION_ID_RANGE = device['nvPairs']['L3_PARTITION_ID_RANGE'],
                            LINK_STATE_ROUTING = device['nvPairs']['LINK_STATE_ROUTING'],
                            LINK_STATE_ROUTING_TAG = device['nvPairs']['LINK_STATE_ROUTING_TAG'],
                            LOOPBACK0_IP_RANGE = device['nvPairs']['LOOPBACK0_IP_RANGE'],
                            LOOPBACK1_IP_RANGE = device['nvPairs']['LOOPBACK1_IP_RANGE'],
                            MULTICAST_GROUP_SUBNET = device['nvPairs']['MULTICAST_GROUP_SUBNET'],
                            NETWORK_VLAN_RANGE = device['nvPairs']['NETWORK_VLAN_RANGE'],
                            OSPF_AREA_ID = device['nvPairs']['OSPF_AREA_ID'],
                            OSPF_AUTH_ENABLE = device['nvPairs']['OSPF_AUTH_ENABLE'],
                            REPLICATION_MODE = device['nvPairs']['REPLICATION_MODE'],
                            RR_COUNT = device['nvPairs']['RR_COUNT'],
                            SERVICE_NETWORK_VLAN_RANGE = device['nvPairs']['SERVICE_NETWORK_VLAN_RANGE'],
                            SUBNET_RANGE = device['nvPairs']['SUBNET_RANGE'],
                            replicationMode = device['replicationMode'],
                            templateName = device['templateName'])
                        device_entry.save()
                aci_model_pruner(dnac_network_device.objects.all(), obj_type="DCNM Fabric", retention_period=30)
            except:
                print('Unable to query devices on DCNM {}'.format(dcnm))


def get_dcnm_network_switch(query_class):
    try:
        devices = dcnm_http_get(query_class)
        for device in devices:
            device_entry=dcnm_network_switch(
                dcnm_addr = dcnm,
                activeSupSlot = device['activeSupSlot'],
                availPorts = device['availPorts'],
                consistencyState = device['consistencyState'],
                cpuUsage = device['cpuUsage'],
                fabricName = device['fabricName'],
                health = device['health'],
                hostName = device['hostName'],
                ipAddress = device['ipAddress'],
                isVpcConfigured = device['isVpcConfigured'],
                licenseViolation = device['licenseViolation'],
                logicalName = device['logicalName'],
                managable = device['managable'],
                memoryUsage = device['memoryUsage'],
                mode = device['mode'],
                model = device['model'],
                network = device['network'],
                numberOfPorts = device['numberOfPorts'],
                present = device['present'],
                release = device['release'],
                serialNumber = device['serialNumber'],
                upTime = device['upTime'],
                vendor = device['vendor'],
                vpcDomain = device['vpcDomain']
                )
            device_entry.save()
        aci_model_pruner(dnac_network_device.objects.all(), obj_type="DCNM Switch", retention_period=30)
    except:
        print('Unable to query devices on DCNM {}'.format(dcnm))


get_dcnm_network_switch('/inventory/switches')
get_dcnm_network_device('/control/fabrics')
