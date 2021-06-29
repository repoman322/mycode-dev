#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
    ## Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )
    
    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)
    
    ## Decode the response
    got_dj = gotresp.json()
    print(f" You selected: {got_dj['name']}")
    for alias in got_dj['aliases']:
        if alias != '':
            print(f"...AKA {alias}")

    try:
        gethouse = got_dj["allegiances"]
        for h in gethouse:
            gothouse = requests.get(h)
            got_hs = gothouse.json()
            print(f"house: {got_hs['name']}")
    except:
        pass

    for book in got_dj["books"]:
        gotbook = requests.get(book)
        got_bk = gotbook.json()
        print(f"book: {got_bk['name']}")

if __name__ == "__main__":
        main()
