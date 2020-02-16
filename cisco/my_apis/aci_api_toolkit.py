from credentials import *
from acitoolkit import acitoolkit
import requests

#connect to apic at htpps://sandboxapicdc.cisco.com and print http status code
session = acitoolkit.Session(URL, LOGIN, PASSWORD)
http_status = session.login()
print ("Logging in to APIC at " + URL + ":")
print (http_status)

#Varibale containing tenant name we wish to use.
tenant_tool = "_Toolkit_Tenant"
tenant_input = input("Input the name for the new Tenant, remember: ")
tenant_name = str(tenant_input + tenant_tool)

#Creating the tenant
new_tenant = acitoolkit.Tenant(tenant_name)

#Commit the new configuration to APIC
commit = session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
print ("Attempting to commit new Tenant to APIC: ")
print (commit)



