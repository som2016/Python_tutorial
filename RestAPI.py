import requests
import json
from requests.auth import HTTPBasicAuth
import pickle

#from getpass import getpass
print('___________________________ Basic POST Request ________________________________________________________________')
print('___________________________ __________________ ________________________________________________________________')
url = 'https://api.github.com/user/repos'
data = {
  "name": "Hello-World2",
  "description": "This is your first repository",
  "homepage": "https://github.com",
  "has_wiki": "true"
}
response = requests.post(url, auth=HTTPBasicAuth('som2016', 'Idea&1234'), verify=False, data=json.dumps(data))
print(response.request.headers)
response.request.headers['Content-Type'] = 'application/json'
print(response.status_code)
print(response.content)
print(response.request.url)
print(response.request.body)
print(response.cookies)
cookie = response.cookies
print('___________________________ __________________ ________________________________________________________________')
print('___________________________ Basic GET Request ________________________________________________________________')
print('___________________________ __________________ ________________________________________________________________')

url = 'https://api.github.com/users/som2016/repos'
response = requests.get(url, cookies=cookie, verify=False,)
print(response.json())
temp = response.json()
#print(json.dumps(temp, sort_keys=True, indent=4)) # sort_keys = True tells the encoder to return the JSON object keys in a sorted order,
with open('data.json', 'w') as f:
    json.dump(temp, f, sort_keys=True, indent=4) # Note here dumps won't work it will give blank file
print('___________________________ __________________ ________________________________________________________________')
print('___________________________ Basic DEL Request ________________________________________________________________')
print('___________________________ __________________ ________________________________________________________________')
url = 'https://api.github.com/repos/som2016/Hello-World'
response = requests.delete(url, cookies=cookie, verify=False,)
print(response.status_code)
print(response.content)

