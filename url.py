from flask import Flask, render_template,request,jsonify,make_response,render_template_string
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)
app.debug = True
@app.route("/")
@app.route("/home")
def home() :
    return render_template("Hello World")

@app.route("/event", methods = ["POST"])
def index():
    return render_template("./codetech.html")





if __name__ == "__main__" :
    app.run(app , debug = True )



