from netmiko import ConnectHandler

with open("command_file") as f:
    commands_to_send = f.read().splitlines()

with open("devices_file") as f:
    devices_list = f.read().splitlines()


for devices in devices_list:
    print ("Connecting to device " + devices)
    device_ip = devices
    ios_device = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": "cisco",
        "password": "cisco"
    }
    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_to_send)
    print(output)



