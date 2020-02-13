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



def create_url(path, controller_ip=DNAC):

    return "https://%s:%s/api/v1/%s" % (controller_ip, DNAC_PORT, path)



def get_url(url):

    url = create_url(path=url)
    print (url)
    token = get_auth_token()
    headers = {"X-auth-token" : token["token"]}
    try:
        response = requests.get(url, headers = headers, verify = False)
    except requests.exceptions.requestException as cerror:
        print ("Error processing request", cerror)
        sys.exit(1)

    return response.json()



def list_network_devices():
    return get_url("network-device")



if __name__ == "__main__":
    response = list_network_devices()
    print ("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".format("hostname", "mgmt IP", "serial", "platformId", "SW Version", "role" "Uptime" ))


    for device in response["response"]:
        uptime = "N/A" if device["upTime"] is None else device["upTime"]
        print ("{0:42}[1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
            format(device["hostname"],
                    device["managementIpAddress"],
                    device["serialNumber"],
                    device["platformId"],
                    device["softwareVersion"],
                    device["role"], uptime))


