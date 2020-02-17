import json
import napalm

driver = napalm.get_network_driver("ios")
device = driver("192.168.122.1", "cisco", "cisco")
device.open()

config = device.get_config()

print (config["running"])


