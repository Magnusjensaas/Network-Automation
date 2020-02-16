import json
from napalm import get_network_driver

driver = get_network_driver("ios")
device = driver(hostname="192.168.122.72", username="cisco", password="cisco")
device.open()

ios_output_bgp = device.get_bgp_neighbors()

print (json.dumps(ios_output_bgp, indent=4))
device.close()

