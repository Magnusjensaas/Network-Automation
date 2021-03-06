import os
import sys
import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

DNAC = "sandboxdnac.cisco.com"
DNAC_USER = "devnetuser"
DNAC_PASSWORD = "Cisco123!"
DNAC_PORT = "443"

def get_auth_token(controller_ip=DNAC, username=DNAC_USER, password=DNAC_PASSWORD):

    login_url = "https://{0}:{1}/dna/system/api/v1/auth/token".format(controller_ip, DNAC_PORT)
    result = requests.post(url=login_url, auth = HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify = False)
    result.raise_for_status()

    token = result.json()["Token"]
    return {
        "controller_ip": controller_ip,
        "token": token
    }


def create_url(path, controller_ip=DNAC):

    return "https://%s:%s/dna/intent/api/v1/%s" % (controller_ip, DNAC_PORT, path)


def get_url(url):

    url = create_url(path = url)
    print (url)
    token = get_auth_token()
    headers = {"X-auth-token" : token["token"]}
    try:
        response = requests.get(url, headers = headers, verify = False)
    except requests.exceptions.RequestsException as cerror:
        print ("Error processing request", cerror)
        sys.exit(1)

    return response.json()


def ip_to_id(ip):

    return get_url("network-device/ip-address/%s" % ip)["response"]["id"]


def get_modules(id):

    return get_url("network-device/module?deviceId=%s" % id)


def print_info(modules):

    print ("{0:30}{1:15}{2:25}{3:5}".format("Module Name", "Serial Number", "Part Number", "Is Field Replaceable?"))
    for module in modules["response"]:
        print ("{moduleName:30}{serialNumber:15}{partNumber:25}{moduleType:5}".format(moduleName=module["name"], serialNumber=module["serialNumber"], partNumber=module["partNumber"], moduleType=module["isFieldReplaceable"]))


if __name__ == "__main__":

    if len(sys.argv) > 1:

        dev_id = ip_to_id(sys.argv[1])
        modules = get_modules(dev_id)

        print_info(modules)

    else:
        print("Usage %s device_ip" % sys.argv[0])

