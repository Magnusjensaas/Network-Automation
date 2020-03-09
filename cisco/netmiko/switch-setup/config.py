import netmiko
import getpass

# Get user input for username and password.
username = input("Username: ")
password = getpass.getpass()


def configure_device(device_type):
    """
    Apply configuration from configuration file.
    """
    if device_type == "dist":
        print("Running distribution setup commands")
        output_config = net_connect.send_config_set(commands_list_dist)
        return print(output_config)
    elif device_type == "acc":
        print("Running access setup commands")
        output_config = net_connect.send_config_set(commands_list_acc)
        return print(output_config)


# Opening file for Switch configuration access.
with open("acc_conf.txt") as f:
    commands_list_acc = f.read().splitlines()

# Opening file fore Switch configuration distribution.
with open("dist_conf.txt") as f:
    commands_list_dist = f.read().splitlines()

# Opening list of devices to apply configurations to.
with open("device-acc.txt") as f:
    devices_acc = f.read().splitlines()

with open("device-dist.txt") as f:
    devices_dist = f.read().splitlines()


if __name__ == "__main__":

    # Loop allowing the commands to be applied to all devices in devices_acc, specifying OS, IP and credentials.
    for devices in devices_acc:
        print("Connecting to device " + devices)
        device_ip = devices
        ios_device = {
            "device_type": "cisco_ios",
            "ip": device_ip,
            "username": username,
            "password": password
        }
        # Try statement with exceptions to catch connectivity issues and credential issues.
        try:
            net_connect = netmiko.ConnectHandler(**ios_device)
        except netmiko.ssh_exception.AuthenticationException:
            print("Authentication failure " + device_ip)
            continue
        except netmiko.ssh_exception.NetMikoTimeoutException:
            print("Connection timed out " + device_ip)
            continue
        except EOFError:
            print("End of file while attempting device " + device_ip)
            continue
        except netmiko.ssh_exception.SSHException:
            print("SSH error " + device_ip)
            continue
        except Exception as unknown_error:
            print(unknown_error)
            continue
        configure_device("acc")
    # Loop allowing for configuration of all devices in device_dist list.
    for devices in devices_dist:
        print("Connecting to device " + devices)
        device_ip = devices
        ios_device = {
            "device_type": "cisco_ios",
            "ip": device_ip,
            "username": username,
            "password": password
        }
        # Try statement with exceptions to catch connectivity issues and credential issues.
        try:
            net_connect = netmiko.ConnectHandler(**ios_device)
        except netmiko.ssh_exception.AuthenticationException:
            print("Authentication failure " + device_ip)
            continue
        except netmiko.ssh_exception.NetMikoTimeoutException:
            print("Connection timed out " + device_ip)
            continue
        except EOFError:
            print("End of file while attempting device " + device_ip)
            continue
        except netmiko.ssh_exception.SSHException:
            print("SSH error " + device_ip)
            continue
        except Exception as unknown_error:
            print(unknown_error)
            continue
        configure_device("dist")
