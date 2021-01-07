#!/bin/python

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# from urllib.request import urlopen
# import urllib
#.request
from bs4 import BeautifulSoup
# import ssl
# 
# # Use the "ssl" library to create a "contex"
# # The ssl contex will be used in urllib's urlopen method
# # The purpose of this context is to ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# 
# # url = input('Enter - ')
# # The sum for the "Sample Data" page is 2553
# url = "http://py4e-data.dr-chuck.net/comments_42.html"
# 
# # old way from py4e's script
# # html = urlopen(url, context=ctx).read()
# 
# # New way
# with urllib.request.urlopen(url, context=ctx) as response:
#    html = response.read()
# 
# soup = BeautifulSoup(html, "html.parser")
# 
# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     # debug
#     junk = input("CTL+c to quit, RTN to continue")
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
