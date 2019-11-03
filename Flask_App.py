from flask import Flask, render_template,request,jsonify,make_response,render_template_string
import flask_excel as excel
from json import dump
from datetime import datetime
import os
import dialogflow_v2
from flask_assistant import ask,tell,build_item,Assistant
from flask_ngrok import run_with_ngrok
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
def welcome_reply():                              #trigger up the name intent used in next action
        speech = 'Microphone check 1,2 नमस्कार!तुम्हारा नाम क्या हे?'
        data = request.get_json(force = True)
        intent = data["queryresult"]["intent"]["Default Welcome Intent"]
        speech = 'Running'
        return tell(speech)

@assist.action('Name')                # name intent is being started
def givenname_query():         # belongs to action of father's occupation
    response1 = print('आपका बहोत धन्य्वाद। अब कृपया मुझे अपने पिता का व्यवसाय बताएं')
    data = request.get_json(force = True)
    intent = data["queryresult"]["intent"]["Name"]
    speech = 'Running'
    return tell(speech)

@assist.action('Fathers-Occupation')   #father's occupation action started
def father_occupation_query():            #triggers up the local(sales) intent
    response2 =  print('अब कृपया मुझे अपनी आज की लोकल चश्मों बिक्री का आंकड़ा बताएं')
    data = request.get_json(force = True)
    intent = data["queryresult"]["intent"]["Fathers-Occupation"]
    speech = 'Running'
    return tell(speech)

@assist.action('Local(sales)')       # local(sales) intent started
def local_Sales_query():           # it triggers nvg-spex
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


def results():
    global itr
    # build a request object
    req = request.get_json(force=True)
            # fetch action of the user
    action = req.get("queryResult").get("queryText")          # this will be a jsonify response form
    call_info[call_ques[itr]] = action
    itr += 1
    if itr == len(call_ques) - 1 :
        with open(file = "C:\\data\\" + "Call Info {}".format(datetime.now().strftime("%d-%m-%Y %H-%M-%S")), mode = "w+") as json_file:
            json_file.write(dump(call_info))


@app.route("/webhook", methods = ["GET", "POST"])                         # so to fetch only hindi data we have to fatch data from
def webhook():                                                      #query text and save it in dataframe in form of array.
    return make_response(jsonify(results()))

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        return jsonify({"result": request.get_array(field_name='file')})
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''


@app.route("/download", methods=['GET'])
def download_file():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv")


@app.route("/take", methods=['GET'])
def export_records():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv",
                                          file_name="export_data")


@app.route("/download_file_named_in_unicode", methods=['GET'])
def download_file_named_in_unicode():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv",
                                          file_name=u"中文文件名")

if __name__ == "__main__" :
    excel.init_excel(app)
    app.run()

itr : int = 0
call_info : dict = dict()
call_ques : list = ["welcome", "name", "fathers_occ", "local_sale", "nvg_sale"]

