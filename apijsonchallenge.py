#!/usr/bin/python3
"""RZFeeser || Alta3 Research
Tracking student inventory within a sqliteDB accessed
via Flask APIs"""

# standard library
import sqlite3 as sql

# python3 -m pip install flask
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

jsondata= []

# return home.html (landing page)
@app.route('/')
def home():
    #return render_template('home.html')
    #return jsonify(jsondata)
    return redirect(url_for("list_students"))

# if someone uses student.html it will generate a POST
# this post will be sent to /addrec
# where the information will be added to the sqliteDB
@app.route('/addrec',methods = ['POST'])
def addrec():
    data = request.json
    try:
        if data:  # json posted as 'data'
            print(data)

            nm = data['nm']         # student name
            addr = data['addr']     # student street address
            city = data['city']     # student city
            pin = data['pin']       # "pin" assigned to student
                                    # ("pin" is just an example of meta data we want to track)
            print(f"Name {nm} POSTED - {data['nm']}")
            # connect to sqliteDB
            with sql.connect("database.db") as con:
                cur = con.cursor()
                print(type(cur))
                # place the info from our form into the sqliteDB
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
                # commit the transaction to our sqliteDB
                con.commit()
            # if we have made it this far, the record was successfully added to the DB
            print("Record successfully added")

    except:
    #    con.rollback()  # this is the opposite of a commit()
        msg = "error in insert operation"    # we were NOT successful

    finally:
        #con.close()     # successful or not, close the connection to sqliteDB
        #return render_template("result.html",msg = msg)    #
        return jsonify(jsondata)

# return all entries from our sqliteDB as HTML
@app.route('/list')
def list_students():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from students")           # pull all information from the table "students"

    rows = cur.fetchall()
    jsondata = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in rows]
    
    print(jsondata)
    return jsonify(jsondata)
    #return render_template("list.html",rows = rows) # return all of the sqliteDB info as HTML

if __name__ == '__main__':
    try:
        # ensure the sqliteDB is created
        con = sql.connect('database.db')
        print("Opened database successfully")
        # ensure that the table students is ready to be written to
        con.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
        print("Table created successfully")
        con.close()
        # begin Flask Application
        app.run(host="0.0.0.0", port=2224, debug = True)
    except:
        print("App failed on boot")
