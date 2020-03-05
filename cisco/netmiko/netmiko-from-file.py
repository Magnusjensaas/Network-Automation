import netmiko
import getpass

# Get user input for username and password.
username = input("Username: ")
password = getpass.getpass()


def check_software_version(device_list):
    """
    Method to check software running on IOS device.
    From list of predefined IOS versions.
    """
    for software_version in device_list:
        print("Checking for software version " + software_version)
        output_version = net_connect.send_command("show version")
        init_version = 0
        int_version = output_version.find(software_version)
        if int_version > 0:
            print("Software version found on device: " + software_version)
            return software_version
        else:
            print("Software not found on device: " + software_version)


def configure_device(software_version):
    """
    Apply configuration from configuration file.
    Applies only the configuration for the software version that is running on the device.
    """
    if software_version == "vios_l2-ADVENTERPRISEK9-M":
        print("Running " + software_version + " Commands")
        output_config = net_connect.send_config_set(commands_list_switch)
        return output_config
    elif software_version == "VIOS-ADVENTERPRISEK9-M":
        print("Running " + software_version + " Commands")
        output_config = net_connect.send_config_set(commands_list_router)
        return output_config


# Opening file for Switch configuration.
with open("commands_list_switch") as f:
    commands_list_switch = f.read().splitlines()

# Opening file fore Router configuration.
with open("commands_list_router") as f:
    commands_list_router = f.read().splitlines()

# Opening file for commands to send to all devices.
with open("command_file") as f:
    commands_to_send = f.read().splitlines()

# Opening list of devices to apply configurations to.
with open("devices_file") as f:
    devices_list = f.read().splitlines()

# Loop allowing the commands to be applied to all devices in devices_list, specifying OS, IP and credentials.
for devices in devices_list:
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

    # Sending configuration from "command_file" and printing the device output.
    device_output = net_connect.send_config_set(commands_to_send)
    print(device_output)

    # List of software version running in my topology
    device_type = ["vios_l2-ADVENTERPRISEK9-M", "VIOS-ADVENTERPRISEK9-M"]

    # Check software version running on device
    software = check_software_version(device_type)

    # Configure device
    output = configure_device(software)
    print(output)
