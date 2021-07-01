#!/usr/bin/python3
from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

# Let the following be the data structure that you want to put inside of a hosts file:

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():

    # render the jinja template "helloname.html"
    # apply the value of username for the var name
    return render_template("temp2.html", gr = groups) # temp2 shows current but adds button for add host
    
# add a new host
@app.route("/new", methods = ["POST"])
def new():
    if request.method == "POST":
        ans = request.form.get("addnew") # indicated by a button click
        if ans == 'add':
            return render_template("addhost.html")
            # add a new host

@app.route("/addhost", methods = ["POST"])
def addhost():
    if request.method == "POST":
        hostname = request.form.get("hostname") # indicated by a button click
        ip = request.form.get("ip")
        fqdn = request.form.get("fqdn")
        answer = {"hostname": hostname,"ip": ip, "fqdn": fqdn}
        groups.append(answer)
        return redirect(url_for("start"))
            
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
   
