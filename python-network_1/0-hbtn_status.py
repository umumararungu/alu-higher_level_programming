#!/usr/bin/python3
#fetching url
import urllib.request
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    html =  response.read()
