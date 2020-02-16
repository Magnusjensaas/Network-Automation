import json
from napalm import get_network_driver

driver = get_network_driver("ios")
ip_list = ["192.168.122.72", "192.168.122.1"]

for ip in ip_list:
    print("Connecting to " + str(ip))
    device = driver(ip, "cisco", "cisco")
    device.open()
    bgp_neighbors = device.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))
    device.close()


