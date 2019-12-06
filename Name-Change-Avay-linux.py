from netmiko import ConnectHandler
from getpass import getpass




Avaya = {
	"username": "admin",
	"password": getpass(),
        "device_type": "linux",
        "ip": "10.40.2.40",
}


net_connect = ConnectHandler(**Avaya)

Telefon_DN = input("Telefonnummer: ")



print (net_connect.find_prompt())
output = net_connect.send_command("cslogin", expect_string="S")
print (output)
output = net_connect.send_command("logi admin", expect_string="PASS?")
print (output)
output = net_connect.send_command(input("Password: "), expect_string=".")
print (output)
output = net_connect.send_command("ld 95", expect_string="C")
print (output)
output = net_connect.send_command("prt", expect_string="TYPE")
print (output)
output = net_connect.send_command("name", expect_string="CUST")
print (output)
output = net_connect.send_command("0", expect_string="CPND")
print (output)
output = net_connect.send_command("", expect_string="PAGE")
print (output)
output = net_connect.send_command("", expect_string="DIG")
print (output)
output = net_connect.send_command("", expect_string="DN")
print (output)
output = net_connect.send_command(str(Telefon_DN), expect_string="DN")
print (output)
output = net_connect.send_command("", expect_string="ENTR")
print (output)
output = net_connect.send_command("", expect_string="REQ")
print (output)
output = net_connect.send_command("out", expect_string="TYPE")
print (output)
output = net_connect.send_command("name", expect_string="CUST")
print (output)
output = net_connect.send_command("0", expect_string="CPND")
print (output)
output = net_connect.send_command("", expect_string="DIG")
print (output)
output = net_connect.send_command("", expect_string="DN")
print (output)
output = net_connect.send_command(str(Telefon_DN), expect_string="DN")
print (output)
output = net_connect.send_command("", expect_string="ENTR")
print (output)
output = net_connect.send_command("", expect_string="MEM")
print (output)
output = net_connect.send_command("new", expect_string="TYPE")
print (output)
output = net_connect.send_command("name", expect_string="CUST")
print (output)
output = net_connect.send_command("0", expect_string="CPND")
print (output)
output = net_connect.send_command("", expect_string="DIG")
print (output)
output = net_connect.send_command("", expect_string="DN")
print (output)
output = net_connect.send_command(str(Telefon_DN), expect_string="NAME")
print (output)
output = net_connect.send_command(input("Navn: "), expect_string="XPLN")
print (output)
output = net_connect.send_command("", expect_string="DISPLAY")
print (output)
output = net_connect.send_command("", expect_string="DN")
print (output)
output = net_connect.send_command("", expect_string="ENTR")
print (output)
output = net_connect.send_command("", expect_string="MEM")
print (output)
print("Navn endret")
input("Press Enter to close: ")