from flask import Flask, render_template,request,jsonify,make_response,render_template_string
from json import dumps
from datetime import datetime
import json
import os
import dialogflow_v2
from flask_assistant import ask,tell,build_item,Assistant
from flask_ngrok import run_with_ngrok
import pandas as pd
import chardet
numb:int = 0
# if True:
    # i+=1
#call_info : dict = dict()
#call_ques : list = ["welcome", "name", "fathers_occ", "local_sale", "nvg_sale"]


app = Flask(__name__)
run_with_ngrok(app)
assist = Assistant(app,project_id="hhr-rdmhqv")

@app.route("/")
@app.route("/home")

def home() :
    return render_template("index.html")
       # to get rich responses from user
app.config["INTEGRATIONS"] = ["Actions On Google"]

#@app.route("/event", methods = ["GET"])          # it gives up the first reply to the user.
#def button_click_event():
#    print("नमस्कार!तुम्हारा नाम क्या हे?")
 #   return render_template_string("Button 1 Clicked!")


@assist.action('Default Welcome Intent')
def givenname_query():                              #trigger up the name intent used in next action
        speech = 'Microphone check 1,2 नमस्कार!तुम्हारा नाम क्या हे?'
        data = request.get_json(force = True)
        intent = data["queryresult"]["intent"]["Default Welcome Intent"]
        speech = 'Running'
        return tell(speech)

@assist.action('Name')                # name intent is being started
def father_occupation_query():         # belongs to action of father's occupation
    response1 = print('आपका बहोत धन्य्वाद। अब कृपया मुझे अपने पिता का व्यवसाय बताएं')
    data = request.get_json(force = True)
    intent = data["queryresult"]["intent"]["Name"]
    speech = 'Running'
    return tell(speech)

@assist.action('Fathers-Occupation')   #father's occupation action started
def local_Sales_query():            #triggers up the local(sales) intent
    response2 =  print('अब कृपया मुझे अपनी आज की लोकल चश्मों बिक्री का आंकड़ा बताएं')
    data = request.get_json(force = True)
    intent = data["queryresult"]["intent"]["Fathers-Occupation"]
    speech = 'Running'
    return tell(speech)

@assist.action('Local(sales)')       # local(sales) intent started
def NVG_sales_query():           # it triggers nvg-spex
    response3 =  print('ठीक है मुझे अपनी आज की NVG  चश्मों की  सेल बताओ')
    data = request.get_json(force = True)
    intent = data["queryresult"]["intent"]["Local(sales)"]
    speech = 'Running'
    return tell(speech)

@assist.action('NVG(sales)')   # NVG(sales) intent is started
def agree_query():                # it triggers up the agree wala intent
    response4 = print('बहुत बहुत धन्यवाद्')
    data = request.get_json(force = True)
    intent = data["queryresult"]["intent"]["NVG(sales)"]
    speech = 'Running'
    return tell(speech)

import codecs
def results():
    global numb
    # build a request object
    req = request.get_json(force=True)
            # fetch action of the user
    act = req.get("queryResult").get("queryText")          # this will be a jsonify response form
    call_info[call_ques[numb]] = act
    numb += 1

    if numb == len(call_ques) :
        with open(file = "C:\\data\\" + "Call_Info {}.json".format(datetime.now().strftime("%d-%m-%Y %H-%M-%S")), mode = "w",encoding='utf-8') as json_file:
            json_file.write(dumps(call_info, indent = 4))
        #nbytes = {'utf-8': 1,'utf-16': 2,'utf-32': 4,}.get(encoding)
        #with open(file = "C:\\data\\" + "Call Info.txt", mode='rt') as txt_file:
            #print to_hex(txt_file.read(), nbytes)


@app.route("/webhook", methods = ["GET", "POST"])                         # so to fetch only hindi data we have to fatch data from
def webhook():                                                      #query text and save it in dataframe in form of array.
    return make_response(jsonify(results()))



if __name__ == "__main__" :
    call_info: dict = dict()
    call_ques: list = ["welcome", "name", "fathers_occ", "local_sale", "nvg_sale"]
    app.run()


from json import load
with open("C:\\data\\Call Info.txt",mode = "r") as txt_file:
    txt_content = load(txt_file)

