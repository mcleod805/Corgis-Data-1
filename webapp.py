from flask import Flask, request, Markup, render_template, Markup
import os
import json
app = Flask(__name__)

@app.route("/PAGE 1")
def render_response():
    state = request.args["Car Companies"]
    return render_template('page1.html',options = get_state_options(), response = your_interesting_demographic_function(state))

@app.route("/home")
def render_response():
    state = request.args["Makes"]
    return render_template('index.html',options = get_state_options(), response = your_interesting_demographic_function(state))
def get_state_options():
    options = ""
    with open('cars.json') as cars_data:
        cars = json.load(cars_data)
    Makes = []
    for c in cars:
        if not c["Make"] in Makes:
              Make.append(c["Make"])
    for s in cars:
       options += Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options
def your_interesting_demographic_function(stateName):
    with open('cars (1).json') as cars_data: 
    return stateName
        
@app.route("/")
def render_main():
    return render_template('index.html')
if __name__== '__main__':
    app.run(debug=True, port=54321)
   
