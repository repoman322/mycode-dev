#!/usr/bin/python3
"""KEggert || FLASK Sample
alta3research-requests02.py should demonstrate proficiency with the requests HTTP library. 
The API you target is up to you, but be sure any data that is returned is "normalized" into 
a format that is easy for users to understand."""
import requests
import re
from random import randrange
import json

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def got_lookup(my_json):
  ## generate random character number between 1-1000
  char = randrange(1,1000)
  ## Send HTTPS GET to the API of ICE and Fire character resource
  gotresp = requests.get(AOIF_CHAR + str(char))
  my_json.append(gotresp.json())  ## Decode the response and add to my_json list
  print(f" Fetching details character {char}: {gotresp.json()['name']}")

def got_details(got_js):
  # pull the char details and format for outout
  # return list of details (json?)
  got_details = []
  url = f"'url': '{got_js['url']}'"
  got_details.append(url)
  aliases = []
  if got_js['aliases'][0] != '':
    for a in got_js['aliases']:
      print(f"...AKA {a}")
      aliases.append(a)
  elif got_js['titles'][0] != '':
    for a in got_js['titles']:
      print(f"...AKA {a}")
      aliases.append(a)
  else:
    aliases.append('None')
    print(f"...Alias and Title not found")
    
  alias = f"'alias': '{aliases}'"
  got_details.append(alias)
  
  if got_js['name'] == "":
    gotchar = got_js['url'][-3:]
    gotchar = re.sub('[!@#$/]', '', gotchar)
    print(f" You selected: character {gotchar}")
    name = f"'name': 'char{gotchar}'"
    got_details.append(name)
  else:
    print(f" You selected: {got_js['name']}")
    name = f"'name': '{got_js['name']}'"
    got_details.append(name)

  if got_js['allegiances'] == "":
    house = "'house': 'None'"
    got_details.append(house)
  else:
    gethouse = got_js["allegiances"]
    print(gethouse)
    houses = []
    for h in gethouse:
      gothouse = requests.get(h)
      got_hs = gothouse.json()
      print(f"house: {got_hs['name']}")
      houses.append(got_hs['name'])
    house = f"'house': '{houses}'"
    got_details.append(house)

  return got_details

## pull names from web and save them to a file for future use
def main():
  my_json = []
  got_list = []
  ## Ask user for input
  got_charCount = input("Pick a number of GoT characters to return info on: " )

  for n in range(1,int(got_charCount)+1):
    ## Send HTTPS GET to the API of ICE and Fire character resource
    got_lookup(my_json)

  for got_js in my_json:
    got_list.append(got_details(got_js))

  print(got_list)  # good json data   
  with open("test.json", 'w') as fout:
    json.dump(got_list, fout)

  for name in got_list:
    print(name[3])
    #for i in name:
    #  print(i)
    
if __name__ == "__main__":
    main()
