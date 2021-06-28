fruitcompanies= [{"name":"Zesty","employees":["Ambu","Brent", "Bryan","Carlee","Chad"]},
                 {"name":"Ripe.ly","employees":["Darlene","Eric","Fernando","Peter",]},
                 {"name":"FruitBee","employees":["Jennae","Joel","Jonas","Josh",]},
                 {"name":"JuiceGrove","employees":["Kurt","Nate","Patrick","Rachel",]}]

def mycompany(coname):
  n = 0
  for i in fruitcompanies:
    #print(f"check for coname {coname} in {i}")
    if coname in i['name']:
      print(f"coname {coname} found at {n}")
      break
    n += 1
    
  for employee in fruitcompanies[n]['employees']:
    print(employee)

def choose_co():
  n = 1
  for co in fruitcompanies:
    print(f"{n}: {co['name']}")
    n += 1
    
  selection = input('Chose a company from the list above (1-4):')
  print(f"Employees for {fruitcompanies[int(selection) - 1]['name']} are:")
  for name in fruitcompanies[int(selection) - 1]['employees']:
    if 'chad' not in name.lower():
      print(name)

def main():

    mycompany('JuiceGrove')
    choose_co()

if __name__ == "__main__":
    main()
