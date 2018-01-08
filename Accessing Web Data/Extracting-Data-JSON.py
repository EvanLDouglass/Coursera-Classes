# Evan Douglass
# Extracting Data from JSON

# This program reads JSON from a webpage and finds information about
# comment counts. The webpage used for this assignment (Coursera) is:
# http://py4e-data.dr-chuck.net/comments_40264.json

import json
from urllib.request import urlopen
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# get info from address
address = input('Enter an address - ')
if address == '':
    quit()
data = urlopen(address).read()

# unpack JSON
data = json.loads(data)

# get total comment count from data
total = 0
for user in data['comments']:
    total = total + user['count']

print('Total comments:', total)
