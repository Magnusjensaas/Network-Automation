import requests
import sys
import json
import click
import tabulate
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.auth import HTTPBasicAuth
from tabulate import tabulate

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


DNAC_IP = "sandboxdnac.cisco.com"
DNAC_USERNAME = "devnetuser"
DNAC_PASSWORD = "Cisco123!"


class rest_api_lib:
    def __init__(self, device_ip, username, password):
        self.device_ip = device_ip
        self.session = {}
        self.login(self.device_ip, username, password)

    def login(self, device_ip, username, password):
        login_url = "https://{0}:{1}/api/system/v1/auth/token".format(device_ip, "443")
        result = requests.post(url=login_url, auth=HTTPBasicAuth(username, password), verify=False)
        result.raise_for_status()

        token = result.json()["Token"]
        return {
            "controller_ip": device_ip,
            "token": token
        }

    def get_request(self, directory):
        """GET request"""
        token = self.login(DNAC_IP, DNAC_USERNAME, DNAC_PASSWORD)
        headers = {"X-auth-token": token["token"]}
        url = "https://%s:443/dna/intent/api/v1/%s" % (DNAC_IP, directory)
        try:
            response = requests.get(url, headers=headers, verify=False)
        except requests.exceptions.requestException as cerror:
            print("Error processing request", cerror)
            sys.exit(1)
        print(url)
        data = response.content
        return data


api_class = rest_api_lib(DNAC_IP, DNAC_USERNAME, DNAC_PASSWORD)


@click.group()
def cli():
    """Command line tool for DNA-Center REST API calls"""
    pass

@click.command()
def get_vlan():

    click.secho("Getting VLAN details")

    response = json.loads(api_class.get_request("topology/vlan/vlan-names"))
    print(type(response))
    print(response)
    data = response["response"]
    print(tabulate([data], headers=['VLAN']))

cli.add_command(get_vlan)


if __name__ == "__main__":
    cli()
