#!/usr/bin/python3
"""Alta3 APIs and HTML"""
# https://opentdb.com/
## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

## This is where we want to redirect users to
@app.route("/success/<answer>")
def success(answer):
    return f" {answer}\n"
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("trivia.html") # look for templates/postmaker.html
    
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location

@app.route("/check", methods = ["POST", "GET"])
def check():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("answer"): # if answer was assigned via the POST
            check_answer = request.form.get("answer") # grab the value of answer from the POST
            if check_answer == '14':
                return redirect(url_for("success", answer = "Correct!!")) # pass back to /success with val for name
            else:
                return redirect(url_for("success", answer = f"sorry, you were WRONG"))
        else: # if a user sent a post without answer then assign value defaultuser
            check_answer = "WRONG"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
