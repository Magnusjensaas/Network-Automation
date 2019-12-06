from netmiko import ConnectHandler

iosv_l2_sw1 = {
	"device_type": "cisco_ios",
	"ip": "192.168.122.72",
	"username": "cisco",
	"password": "cisco",
}

iosv_l2_sw2 = {
	"device_type": "cisco_ios",
	"ip": "192.168.122.82",
	"username": "cisco",
	"password": "cisco",
}

iosv_l2_sw3 = {
	"device_type": "cisco_ios",
	"ip": "192.168.122.83",
	"username": "cisco",
		"password": "cisco",
}

all_devices = [iosv_l2_sw1, iosv_l2_sw2, iosv_l2_sw3]


for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	for n in range (2,21):
		print ("creating VLAN " + str(n))
		config_commands = ["vlan " + str(n), "name Python_Vlan " + str(n)]
		output = net_connect.send_config_set(config_commands)
		print (output)
