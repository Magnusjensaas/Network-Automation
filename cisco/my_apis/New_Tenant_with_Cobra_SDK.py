from credentials import *
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol

#Connection to the APIC
auth = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
session = cobra.mit.access.MoDirectory(auth)
connect = session.login()

#Define the name of the new Tenant with user input.
tenant_cobra = "_Cobra_Tenant"
tenant_input = input("Input a name for the new Tenant here: ")
tenant_name = str(tenant_input + tenant_cobra)


#Creating the Tenant configuration
root = cobra.model.pol.Uni("")
new_tenant = cobra.model.fv.Tenant(root, tenant_name)

#Commiting the new Tenant to the APIC
config_request = cobra.mit.request.ConfigRequest()
config_request.addMo(new_tenant)
commit = session.commit(config_request)
print ("Attempting to add the new Tenant to: ", URL)
print (commit)


