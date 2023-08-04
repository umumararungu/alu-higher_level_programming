#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""
import urllib.request
with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
    html =  response.read()
