import requests
from pprint import pprint

apiUrl = "https://api.ciscospark.com/v1/rooms"
access_token = "NzhlYzg0MGItYjg4Mi00NjFkLTgyZWUtM2M3YzFiZTU1YTA3NjY1NmEyNzQtMDZj_PF84_0deaf262-44a0-4228-b754-9e42428b40fe"

httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
queryParams = {"sortBy" : "lastactivity", "max" : "2"}

response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

print (response.status_code)
pprint(response.json())


