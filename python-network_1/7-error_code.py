#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)'"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print("{}".format(response.text))
