import requests
from  pprint import pprint

access_token = "NzhlYzg0MGItYjg4Mi00NjFkLTgyZWUtM2M3YzFiZTU1YTA3NjY1NmEyNzQtMDZj_PF84_0deaf262-44a0-4228-b754-9e42428b40fe"
apiUrl = "https://api.ciscospark.com/v1/messages"

httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
json_payload = {"roomId" : "Y2lzY29zcGFyazovL3VzL1JPT00vMmYxZjFiZTAtNTAzOC0xMWVhLWFiYTUtZWYwMmM4MDhkOWY4", "text" : "hey.."}

response = requests.post(url=apiUrl, json=json_payload, headers=httpHeaders)

print (response.status_code)
pprint(response.json())


