from netmiko import ConnectHandler
from getpass import getpass

Avaya = {
	"username": "admin",
	"password": getpass(),
        "device_type": "linux",
        "ip": "10.40.2.40",
}

net_connect = ConnectHandler(**Avaya)

print (net_connect.find_prompt())
output = net_connect.send_command("cslogin", expect_string="S")
print (output)
output = net_connect.send_command("****", expect_string="PASS?")
print (output)
output = net_connect.send_command(input ("Balder_123"), expect_string=".")
print (output)
output = net_connect.send_command("ld 20", expect_string="PT0000")
print (output)
output = net_connect.send_command("prt", expect_string="TYPE:")
print (output)
output = net_connect.send_command("dnb", expect_string="CUST")
print (output)
output = net_connect.send_command("0", expect_string="DN")
print (output)
output = net_connect.send_command(input("Intern-nummer Ålesund: "), expect_string="DATE")
print (output)
output = net_connect.send_command("", expect_string="PAGE")
print (output)
output = net_connect.send_command("", expect_string="DES")
print (output)
output = net_connect.send_command("", expect_string="DN")
print (output)