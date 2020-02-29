import requests
import sys
import json
import click
import tabulate
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

SDWAN_IP = "sandboxsdwan.cisco.com"
SDWAN_USERNAME = "devnetuser"
SDWAN_PASSWORD = "Cisco123!"

if SDWAN_IP is None or SDWAN_USERNAME is None or SDWAN_PASSWORD is None:
    print("SDWAN credentials or IP missing")
    exit("1")


class rest_api_lib:
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        self.login(self.vmanage_ip, username, password)

    def login(self, vmanage_ip, username, password):
        """Login to vmanage"""
        base_url_str = "https://%s:8443/" % vmanage_ip
        login_action = "j_security_check"

        # Format data for loginForm
        login_data = {"j_username": username, "j_password": password}

        # URL for posting login data
        login_url = base_url_str + login_action

        sess = requests.session()
        login_response = sess.post(url=login_url, data=login_data, verify=False)

        if b"<html>" in login_response.content:
            print("Login Failed")
            sys.exit()
        self.session[vmanage_ip] = sess

    def get_request(self, mount_point):
        """GET request"""
        url = "https://%s:8443/dataservice/%s" % (self.vmanage_ip, mount_point)
        print(url)
        response = self.session[self.vmanage_ip].get(url, verify=False)
        data = response.content
        return data

    def post_request(self, mount_point, payload, headers={"Content-Type": "application/json"}):
        """POST request"""
        url = "https://%s;8443/dataservice/%s" % (self.vmanage_ip, mount_point)
        payload = json.dumps(payload)
        print(payload)

        response = self.session[self.vmanage_ip].post(url=url, data=payload, headers=headers, verify=False)
        data = response.json()
        return data


sdwanp = rest_api_lib(SDWAN_IP, SDWAN_USERNAME, SDWAN_PASSWORD)


@click.group()
def cli():
    """Command line tool for deploying templates to CISCO SD-WAN"""
    pass


@click.command()
def device_list():
    """Retrieve and return network devices list.

       Returns information about each device that is part of the fabric.

       Example command:
            ./sdwan.py device-list
    """
    click.secho("Retrieving the devices")

    response = json.loads(sdwanp.get_request("device"))
    items = response["data"]

    headers = ["Host-Name", "Device Type", "Device ID", "System IP", "Site ID", "Version", "Device Model"]
    table = list()

    for item in items:
        tr = [item["host-name"], item["device-type"], item["uuid"], item["system-ip"], item["site-id"], item["version"],
              item["device-model"]]
        table.append(tr)
        try:
            click.echo(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
        except UnicodeEncodeError:
            click.echo(tabulate.tabulate(table, headers, tablefmt="grid"))


@click.command()
def template_list():
    """Retrieve and return templates list.

       Returns the templates available ont he vManage instance

       Example command:

            ./sdwan.py template-list

    """
    click.secho("Retrieving the templates available")

    response = json.loads(sdwanp.get_request("template/device"))
    items = response["data"]

    headers = ["Template Name", "Device Type", "Template ID", "Attached devices", "Template version"]
    table = list()

    for item in items:
        tr = [item["templateName"], item["deviceType"], item["templateId"], item["devicesAttached"],
              item["templateAttached"]]
        table.append(tr)
    try:
        click.echo(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        click.echo(tabulate.tabulate(table, headers, tablefmt="grid"))


@click.command()
@click.option("--template", help="Name of the template you wish to retrieve in formation for")
def attached_devices(template):
    """Retrieve and return devices associated to a template.

       Example command:

            ./sd-wan.py attached-devices --template abcd1234

    """

    url = "template/device/config/attached/{0}".format(template)

    response = json.loads(sdwanp.get_request(url))
    items = response["data"]

    headers = ["Host Name", "Device IP", "Site ID", "Host ID", "Host Type"]
    table = list()

    for item in items:
        tr = [item["host-name"], item["deviceIP"], item["site-id"], item["uuid"], item["personality"]]
        table.append(tr)
    try:
        click.echo(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        click.echo(tabulate.tabulate(table, headers, tablefmt="grid"))


@click.command()
def attach():
    pass


@click.command()
def detach():
    pass


cli.add_command(attach)
cli.add_command(detach)
cli.add_command(device_list)
cli.add_command(attached_devices)
cli.add_command(template_list)

if __name__ == "__main__":
    cli()
