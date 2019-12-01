import requests
import json
from requests.auth import HTTPBasicAuth
import re


# Dumps-> Convert from Python to JSON
# Loads -> Parse JSON - Convert from JSON to Python
# If you want to dump the JSON into a file/socket or whatever,
# then you should go for dump(). If you only need it as a string (for printing, parsing or whatever) then use dumps() (dump string)

list1, url_list, url_list2 = [], [], []
fp = open('Passwords.txt', 'r')
for line in fp:
    temp = re.sub('[\n]', '', line)
    list1.append(temp)
url = 'https://api.github.com/users/som2016/repos'
login = requests.session()
login.auth = HTTPBasicAuth(list1[0], list1[1])
response = login.get(url, verify=False)
temp = response.json()
output = json.dumps(temp, indent=4)
print(output)
print('___________________________ __________________ ________________________________________________________________')
print('___________________________ Basic Json Parser ________________________________________________________________')
print('___________________________ __________________ ________________________________________________________________')
print(type(temp))
print(json.dumps(temp[0], indent=4))
output_converted = json.loads(output)
x = 0
for i in output_converted:      # We can directly use temp which is converted to json via response.json().
                                # json.dumps converted to python and the json.loads converted that back to json
#    print(i)
#    print(output_converted[x]['owner'])
    url_list.append(output_converted[x]['git_url'])
    temp = output_converted[x]['owner']
    url_list2.append(temp['avatar_url'])
    x = x+1

print(url_list)
print(url_list2)