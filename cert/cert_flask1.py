#!/usr/bin/python3
"""KEggert || FLASK Sample
alta3research-flask01.py should demonstrate proficiency with the flask library. Ensure your application has at 
least two endpoints. At least one of your endpoints should return legal JSON.
This will be a simple database of GoT characters.
"""

# standard library
import sqlite3 as sql
import json

# python3 -m pip install flask
from flask import Flask, redirect, url_for, render_template, request, jsonify

app = Flask(__name__)

jsondata= []

# return home.html (landing page)
@app.route('/')
def home():
    return render_template('home.html')
    #return redirect(url_for("list_students"))

# return character.html (a way to add a student to our sqliteDB)
@app.route('/enternew')
def new_char():
    return render_template('character.html')

# if someone uses character.html it will generate a POST
# this post will be sent to /addchar
# where the information will be added to the sqliteDB
@app.route('/addchar',methods = ['POST'])
def addchar():
    try:
        nm = request.form['nm']         # character name
        ali = request.form['ali']       # charater alias or title
        hs = request.form['hs']         # house allegiances
        url = request.form['url']       # url of the character information details
                                    
        print(f"Name {nm} POSTED - {request.form['nm']}")
        db_update(nm,ali,hs,url)
            
    except:
        msg = "error in insert operation"    # we were NOT successful

    finally:
        #return jsonify(jsondata)
        return redirect(url_for("home"))
       
@app.route('/load')    
def bulk_load():
    with open(r"test.json", "r") as read_file:
        data = json.load(read_file)
        #print(data)

        for char in data:
            #print(char)
            print(type(char)) # type is dict
            #print(char['name'])
            
            nm = char['name']         # character name
            ali = char['alias']       # charater alias or title
            hs = char['house']         # house allegiances
            url = char['url']       # url of the character information details
                                    
            print(f"Name {nm} POSTED - {char['name']}")
            db_update(nm,ali,hs,url)    
            
        return redirect(url_for("home"))
    
@app.route('/json')    
def show_json():
    con = sql.connect("got.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from characters")           # pull all information from the GoT table "characters"

    rows = cur.fetchall()
    jsondata = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in rows]
    
    print(jsondata)
    return jsonify(jsondata)
  
@app.route('/list')    
def list_names():
    con = sql.connect("got.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("SELECT * from characters")           # pull all information from the GoT table "characters"
    
    rows = cur.fetchall()
    return render_template("got_list.html",rows = rows) # return all of the sqliteDB info as HTML

def db_update(nm,ali,hs,url):
    # connect to sqliteDB
    with sql.connect("got.db") as con:
        cur = con.cursor()
        print(type(cur))
        # place the info from our form into the sqliteDB
        cur.execute("INSERT INTO characters (name,alias,allegiances,url) VALUES (?,?,?,?)",(nm,ali,hs,url) )
        # commit the transaction to our sqliteDB
        con.commit()
    # if we have made it this far, the record was successfully added to the DB
    print("Record successfully added")
  
if __name__ == '__main__':
    try:
        # ensure the sqliteDB is created
        con = sql.connect('got.db')
        print("Opened database successfully")
        # ensure that the table names is ready to be written to
        con.execute('CREATE TABLE IF NOT EXISTS characters (name TEXT, alias TEXT, allegiances TEXT, url TEXT)')
        print("Table created successfully")
        con.close()
        # begin Flask Application
        app.run(host="0.0.0.0", port=2224, debug = True)
    except:
        print("App failed on boot")

