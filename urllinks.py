#!/bin/python3

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
SslContex = ssl.create_default_context()
SslContex.check_hostname = False
SslContex.verify_mode = ssl.CERT_NONE

def GetSoup(url,ctx):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

InitialUrl = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

# ForLoopUrl
flu=""

for i in range(4):

    if not flu:
        tags = GetSoup(InitialUrl,SslContex).find_all('a')
    else:
        tags = GetSoup(flu,SslContex).find_all('a')

    flu = tags[2].get('href', None)

print( flu.split("_")[-1].split(".")[0] )

# Retrieve all of the anchor tags
# tags = soup.find_all('a')
# for tag in tags:
#    print(tag.get('href', None))
