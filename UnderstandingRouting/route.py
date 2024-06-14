# Name:Tala khaled
# email:talakh1798@gmail.com
# desc:building a server with Flask from scratch

from flask import Flask

app=Flask(__name__)

@app.route("/")
def Hello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/hi/<name>")
def persons(name):
    return f"Hi {name}!" 

@app.route("/repeat/<int:num>/<string:word>")
def repeat(num,word):
    return num*word

if __name__=="__main__":
    app.run(debug=True,port=5000)