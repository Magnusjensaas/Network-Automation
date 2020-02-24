from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.72",
    "username": "cisco",
    "password": "cisco"
}

net_connect = ConnectHandler(**device)
output = net_connect.send_command("show ip int brief")
print(output)



