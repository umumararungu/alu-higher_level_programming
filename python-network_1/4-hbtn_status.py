#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

import requests

if __name__ == '__main__':
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
