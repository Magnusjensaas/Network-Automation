import threading
from getpass import getpass
from pprint import pprint
from netmiko import ConnectHandler
from time import time


def read_devices(devices_filename):
    devices = {}  # Dict to store device info.
    with open(devices_filename, "r") as devices_file:  # Open specified file.
        for device_line in devices_file:  # For loop to loop trough lines in file.
            device_info = device_line.strip().split(",")  # Extract device info from line
            device = {"ipaddr": device_info[0],
                      "type": device_info[1],
                      "name": device_info[2]}  # Dict containing device information.
            devices[device["ipaddr"]] = device  # Add key "device" to devices with value device.
        print("\n-----Devices-----")
        pprint(devices)  # Pretty-print devices Dict.
        return devices


def determine_device(device):
    # if condition to check if device type is supported.
    if device["type"] == "cisco_ios":
        device_type = "cisco_ios"
        return device_type
    else:
        print("Unknown device type, supported device types: cisco_ios")


def session_create(device):
    device_type = determine_device(device)
    session = ConnectHandler(device_type=device_type, ip=device["ipaddr"],
                             username=username, password=password)
    return session


def config_device(device):
    device_type = determine_device(device)
    session = session_create(device)
    if device_type == "cisco_ios":
        print("Connecting to device {0}".format(device))
        config_data = session.send_command("show run")
        return config_data


def write_to_file(device):
    config_data = config_device(device)
    session = session_create(device)
    config_filename = "config-" + device["ipaddr"]
    print("Writing configuration: ", config_filename)
    with open(config_filename, "w") as config_out: config_out.write(config_data)

    session.disconnect()


def run(device):
    determine_device(device)
    session_create(device)
    write_to_file(device)


if __name__ == "__main__":
    devices = read_devices("device-file")  # Read device information from file.
    # Obtain credentials.
    username = "cisco"
    password = getpass()
    # Start timer.
    starting_time = time()

    config_threads_list = []

    for ipaddr, device in devices.items():
        print("Getting config for: ", device)
        config_threads_list.append(threading.Thread(target=run, args=(device,)))

    for config_thread in config_threads_list:
        config_thread.start()

    for config_thread in config_threads_list:
        config_thread.join()
