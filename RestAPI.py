import requests
import json
from requests.auth import HTTPBasicAuth
import re
#from getpass import getpass            ## to take passwords without displaying it
list1 = list()
fp = open('Passwords.txt', 'r')
for line in fp:
    temp = re.sub('[\n: \t]', '', line)
    list1.append(temp)

# Dumps-> Convert from Python to JSON
# Loads -> Parse JSON - Convert from JSON to Python

print('___________________________ __________________ ________________________________________________________________')
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
login.auth= HTTPBasicAuth(list1[0], list1[1])
response = login.post(url,  verify=False, data=json.dumps(data))    ##Verify false as SSL Certificate check false else give the path
#response.request.headers['Content-Type'] = 'application/json'      ## Without this its still working
#print(response.request.header)
print(response.status_code)
print(response.content)
print(response.request.url)
print(response.request.body)


print('___________________________ __________________ ________________________________________________________________')
print('___________________________ Basic GET Request ________________________________________________________________')
print('___________________________ __________________ ________________________________________________________________')

url = 'https://api.github.com/users/som2016/repos'
response = login.get(url, verify=False,)
print(response.json())
temp = response.json()
print(json.dumps(temp, sort_keys=True, indent=4))         ## sort_keys = True tells the encoder to return the JSON object keys in a sorted order,
with open('data.json', 'w') as f:                          ## Data.json is the new file name
    json.dump(temp, f, sort_keys=True, indent=4)           ## Note here json.dumps() won't work it will give blank file



print('___________________________ __________________ ________________________________________________________________')
print('___________________________ Basic DEL Request ________________________________________________________________')
print('___________________________ __________________ ________________________________________________________________')
url = 'https://api.github.com/repos/som2016/Hello-World3'   ## It works even though 1st task gets failed due to some HTTP error
response = login.delete(url, verify=False,)
print(response.status_code)
print(response.content)

