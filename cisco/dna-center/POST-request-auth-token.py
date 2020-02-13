import requests
from requests.auth import HTTPBasicAuth

DNAC = "sandboxdnac.cisco.com"
DNAC_USER = "devnetuser"
DNAC_PASSWORD = "Cisco123!"
DNAC_PORT = "443"

def get_auth_token(controller_ip=DNAC, username=DNAC_USER, password=DNAC_PASSWORD):

    login_url = "https://{0}:{1}/api/system/v1/auth/token".format(controller_ip, DNAC_PORT)
    result = requests.post(url=login_url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify = False)
    result.raise_for_status()

    token = result.json()["Token"]
    return {
        "controller_ip": controller_ip,
        "token": token
    }

