import json
import napalm

#Defines the OS running on the device we wish to target in this case IOS, sets parameters for connection, IP, USR, PSWD and opens the connection.
driver = napalm.get_network_driver("ios")
device = driver("192.168.122.72", "cisco", "cisco")
device.open()

#Prints connecting message, uploads .cfg file, commits the file to the running config and closes the connection.
print ("Connecting to 192.168.122.72")
device.load_merge_candidate(filename="ACL1.cfg")
device.commit_config()
device.close()
