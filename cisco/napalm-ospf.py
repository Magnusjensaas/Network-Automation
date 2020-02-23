import json
import napalm

#Defining operatingsystem of network device (IOS), defining IP, USR, PSWD and opening connection.
driver = napalm.get_network_driver("ios")
device = driver("192.168.122.72", "cisco", "cisco")
device.open()

#Prints connecting message and uploads .cfg file to be merged to devices running config.
print ("Accessing device 192.168.122.72")
device.load_merge_candidate(filename="ospf1.cfg")

#Compare uploaded .cfg file to running config on device.
diffs = device.compare_config()

#Commits config that does not exist on the device and discards config already in use.
if len(diffs) > 0:
    print (diffs)
    device.commit_config()
else:
    print ("Configuration is already in use, exiting")
    device.discard_config()

#Closes connection.
device.close()




