import json
import napalm

driver = napalm.get_network_driver("ios")
device = driver("192.168.122.72", "cisco", "cisco")
device.open()

print ("Connecting to 192.168.122.72")
device.load_merge_candidate(filename="ACL1.cfg")
device.commit_config()
device.close()
