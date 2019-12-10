from netmiko import ConnectHandler
from getpass import getpass

ios = {
	"device_type": "cisco_ios",
	"ip": "1.1.1.1",
	"username": input("Username: "),
	"password": getpass(),
}

vlan = input("Input the VLAN in need of IP-helper: ")


net_connect = ConnectHandler(**ios)

if (1==1):
    print("Configuring IP-Helper on VLAN" + str(vlan))
    config_commands = ["interface vlan " + str(vlan), "ip helper A.B.C.D", "end", "show run int vlan " + str(vlan), "write"]
    output = net_connect.send_config_set(config_commands)
    print(output)
