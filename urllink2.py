#!/bin/python3

from bs4 import BeautifulSoup # Install bs4: pip3 install bs4
import urllib
import ssl
 
# Use the "ssl" library to create a "contex"
# The ssl contex will be used in urllib's urlopen method
# The purpose of this context is to ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("This sum should end in 37")

url = "http://py4e-data.dr-chuck.net/comments_1123608.htmli"

with urllib.request.urlopen(url, context=ctx) as response:
   html = response.read()

soup = BeautifulSoup(html, "html.parser")

print("this scripts sum:", sum( int(x.text) for x in soup.find_all('span') ) )

# Pull out all "span" tags
# soup.find_all('span')

# Use the "text" method to get the number (as a string) out of a span tag
# x.text

## debug for each print(tags)junk = input("CTL+c to quit, RTN to continue")
