import requests
import json
from requests.auth import HTTPBasicAuth

#from getpass import getpass
print('___________________________ Basic POST Request ________________________________________________________________')
print('___________________________ __________________ ________________________________________________________________')
url = 'https://api.github.com/user/repos'
data = {
  "name": "Hello-World3",
  "description": "This is your first repository",
  "homepage": "https://github.com",
  "has_wiki": "true"
}
login = requests.session()
login.auth= HTTPBasicAuth('som2016', 'Idea&1234')
response = login.post(url,  verify=False, data=json.dumps(data))
print(response.request.headers)
print(response.status_code)

print('___________________________ __________________ ________________________________________________________________')
print('___________________________ Basic DEL Request ________________________________________________________________')
print('___________________________ __________________ ________________________________________________________________')
url = 'https://api.github.com/repos/som2016/Hello-World3'
response = login.delete(url, verify=False,)
print(response.status_code)
print(response.content)

