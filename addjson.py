#!/usr/bin/python3

import requests
import json

data = {
    "nm" : "Wade Wilson",
    "addr" : "Planet Earth",
    "city" : "Beantown",
    "pin" : "5555",
}

URL = "http://10.4.10.44:2224/addrec"

requests.post(URL, json=data)
