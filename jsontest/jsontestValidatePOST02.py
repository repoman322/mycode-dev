#!/usr/bin/python3
"""
PART D format the data in the following manner: {"json": "time: <<PART A>>, ip: <<PARTB>>, mysvrs: [ <<PARTC>> ]"}
PART E Validate your JSON with a POST
"""

import requests
import datetime
import json

def get_ip():
    IPURL = "http://ip.jsontest.com/"
    # use requests library to send an HTTP GET
    resp = requests.get(IPURL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "ip"
    print(f"The current WAN IP is --> {respjson['ip']}")
    return respjson['ip']
    
def get_hosts(hostfile):
    host_list = []
    with open(hostfile, 'r') as hf:  # this will read each line in the file, one at a time 
        # indent to keep the file object open
        # loop across the lines in the file
        for host in hf:
            host_list.append(host.rstrip("\n"))  ## add host name but remove the newline
            
    # no need to close the file - closed automatically
    return host_list 

def valid_j(mydata):
    # define the URL we want to use
    POSTURL = "http://validate.jsontest.com/"
    
    # use requests library to send an HTTP POST
    resp = requests.post(POSTURL, data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

def main():
    rightnow = datetime.datetime.today().strftime('%Y%m%d')
    print(f"It is now: {rightnow}")
    myip = get_ip()
    print(type(myip))
    print(myip)
    mydata = {"json": "{'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}" }
    valid_j(mydata)
    #hosts = get_hosts('myservers.txt')
    hosts = get_hosts('jsontest/myservers.txt')
    js = {"json": "{'time': rightnow, 'ip': myip, 'mysrvs': [hosts]}"}
    print(js)
    valid_j(js)

    js2 = {"json": {"time": rightnow, "ip": myip, "mysrvs": hosts}}
    print(js2)
    valid_j(js2)
    js3 = {
        "json": {
            "time": rightnow,
            "ip": myip,
            "mysrvs": hosts
            }
          }
    print(js3)
    valid_j(js3)

if __name__ == "__main__":
    main()
