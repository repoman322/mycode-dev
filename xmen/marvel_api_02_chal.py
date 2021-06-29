#!/usr/bin/env python3
"""Marvel Python Client
RZFeeser@alta3.com | Alta3 Research"""

# standard library imports
import argparse   # pull in arguments from CLI
import time       # create time stamps (for our RAND)
import hashlib    # create our md5 hash to pass to dev.marvel.com
from pprint import pprint # we only want pprint() from the package pprint

# 3rd party imports
import requests   # python3 -m pip install requests

## Define the API here
API = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(rand, privkey, pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest()  # create an MD5 hash of our identifers

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(rand, keyhash, pubkey, lookmeup):
    r = requests.get(f"{API}?name={lookmeup}&ts={rand}&apikey={pubkey}&hash={keyhash}")  # send an HTTP GET to this location

    # the marvel APIs are "flakey" at best, so check for a 200 response
    if r.status_code != 200:
        response = None     #
    else:
        response = r.json()

    # return the HTTP response with the JSON removed
    return response

    
def main():

    ## harvest private key
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip('\n')

    ## harvest public key
    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('\n')

    ## create an integer from a float timestamp (for our RAND)
    rand = str(time.time()).rstrip('.')

    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    keyhash = hashbuilder(rand, privkey, pubkey)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    result = marvelcharcall(rand, keyhash, pubkey, args.hero)

    ## display results
    #pprint(result)
    char_data = result['data']
    # How many comics did they appear in?
    count = char_data['results'][0]['comics']['available']
    print(f"Comic count is listed as {count}")
    listem = char_data['results'][0]['comics']['items']
    #print(f"list contains {len(listem)} items")
    
    # last 5 titles
    print(f"Here are some comics {args.hero} appears in:")
    for i in listem[:5]:
        print(i['name'])
    # Some other detail of my choice
    print(f"{args.hero} appears in: {result['data']['results'][0]['stories']['available']} stories as well")
    # backstory if provided
    if char_data['results'][0]['description'] != '':
        print("Here is the description provided:")
        print(f"{char_data['results'][0]['description']}")
    else:
        print("so sad, no character description is available...")
    # download picture to /home/student/static  directory

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # This allows us to pass in public and private keys
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')

    ## This allows us to pass the lookup character
    parser.add_argument('--hero', help='Character to search for within the Marvel universe')
    args = parser.parse_args()
    main()  
