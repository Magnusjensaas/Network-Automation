import json
import napalm

#Defines the OS running on the device we wish to target in this case IOS, sets parameters for connection, IP, USR, PSWD and opens the connection.
driver = napalm.get_network_driver("ios")
device = driver("192.168.122.72", "cisco", "cisco")
device.open()

#Prints connecting message and uploads .cfg file
print ("Connecting to 192.168.122.72")
device.load_merge_candidate(filename="ACL1.cfg")

#Checks if config file has differencing config from running config
diffs = device.compare_config()


#Commits the config to running if the running config does not contatin the loaded config and discards if config is alreadt in place.
if len(diffs) > 0:
    print (diffs)
    device.commit_config()
else:
    print ("This configuration is already in use")
    device.discard_config()

#Closes connection to device.
device.close()


