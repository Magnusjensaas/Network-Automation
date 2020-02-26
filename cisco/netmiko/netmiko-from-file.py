import netmiko
import getpass

username = input("Username: ")
password = getpass.getpass()

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
        "username": username,
        "password": password
    }
    try:
        net_connect =netmiko.ConnectHandler(**ios_device)
    except (netmiko.ssh_exception.AuthenticationException):
        print("Authentication failure " + device_ip)
        continue
    except(netmiko.ssh_exception.NetMikoTimeoutException):
        print("Connection timed out " + device_ip)
        continue
    except(EOFError):
        print("End of file while attempting device " + device_ip)
        continue
    except(netmiko.ssh_exception.SSHException):
        print("SSH error " + device_ip)
        continue
    except Exception as unknown_error:
        print(unknown_error)
        continue


       
    output = net_connect.send_config_set(commands_to_send)
    print(output)



