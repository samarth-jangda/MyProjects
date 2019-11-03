# import flask dependencies
from flask import Flask, request, make_response, jsonify
from flask_assistant import ask,tell,event,build_item,Assistant
 #from flask_ngrok import Assistant,ask
# initialize the flask app
@assist.route("/")
@assist.route("/home")

def home() :
    return render_template("index.html")

app = Flask(__name__)
assist = Assistant(app)
# run_with_ngrok(app)

@assist.action('Name')
  def hello_world():
    speech = 'Microphone check 1,2 what is this'

@ assist.action('Fathers-Occupation')
  def FatherOccupation():
    return tell('अब कृपया मुझे अपनी आज की लोकल चश्मों बिक्री का आंकड़ा बताएं')
@ assist.action('')

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get("queryResult").get("action")

    # return a fulfillment response
    return {"fulfillmentText": "hi, webhook here! :D"}


# create a route for webhook
@app.route("/webhook", methods = ["GET", "POST"])
def webhook():
    return make_response(jsonify(results()))


# run the app
if __name__ == "__main__":
   app.run(debug = True)
   app.run('localhost',8000)