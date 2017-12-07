from flask import Flask, request, Markup, render_template, Markup
import os
import json
app = Flask(__name__)

@app.route("/home")
def render_response():
    state = request.args["states"]
    return render_template('home.html',options = get_state_options(), response = your_interesting_demographic_function(state))
def get_state_options():
    options = ""
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    state = []
    for c in counties:
        if not c["State"] in state:
              state.append(c["State"])
    for s in state:
       options += Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options
def your_interesting_demographic_function(stateName):
    with open('county_demographics.json') as demographics_data: 
        counties = json.load(demographics_data)
        number = 0
        total = 0
        for c in counties:
            if c["State"] == stateName:
                total  += c["Income"]["Median Houseold Income"]
                number+=1
        return (total/number)
@app.route("/")
def render_main():
    return render_template('home.html',options = get_state_options())
if __name__=="__main__":
    app.run(debug=True, port=54321)
