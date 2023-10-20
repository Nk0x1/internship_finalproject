# https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/births/

# call api, parse response

import requests
from flask import Flask,render_template, request
app=Flask(__name__)


@app.route('/')
def enter():
    return render_template("index.html")



@app.route('/result', methods=["POST"])
def result():
    if request.method=="POST":
        data = request.form['dob']
        response=requests.get(f"https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/births/{data}")
        details=response.json()
        return render_template('final.html',details = details) 
           
            

if __name__=="__main__":    
    app.run(debug=True)
  

