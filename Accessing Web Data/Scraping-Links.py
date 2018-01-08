# Evan Douglass
# Scraping Links from HTML

# This program scrapes links from a website's HTML using Beautiful Soup
# and the url library in Python. It follows a trail of links starting
# at the initial page. The link used for this assignment is:
# http://py4e-data.dr-chuck.net/known_by_Keatin.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# get first url, the link position to follow, and how many times to follow
url = input('Enter url - ').strip()
position = int(input('Enter position of interest - '))
num_times = int(input('How many links should I follow - '))

# cycle through links until we reach the desired location
for _ in range(num_times):
    html = urlopen(url, context=ctx).read()

    # get and clean HTML
    soup = BeautifulSoup(html, 'html.parser')

    # retrieve all anchor tags
    tags = soup('a')

    # get the link in desired postion
    link = tags[position - 1].get('href')
    url = link
    print(url)
