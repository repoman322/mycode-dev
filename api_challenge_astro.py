#!/usr/bin/env python3
import requests

ASTRO = "http://api.open-notify.org/astros.json"

def main():
    
    ## Send HTTPS GET to the API of ICE and Fire character resource
    astresp = requests.get(ASTRO)
    
    ## Decode the response
    astr = astresp.json()
    print(astr)
    print(f"People in space: {len(astr['people'])}")
    for person in astr['people']:
        print(f" {person['name']} is on {person['craft']}")

if __name__ == '__main__':
    main()
