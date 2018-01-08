# Evan Douglass
# Calling a JSON API

# This program finds information from a geographical API similar to
# Google's

import json
import urllib.request, urllib.parse, urllib.error

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

# loop allows multiple uses of program without running again
while True:
    address = input('Enter location - ')
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    print(json.dumps(js, indent=2))

    place = js['results'][0]['place_id']
    print('The place id for', address, 'is', place)
