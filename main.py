#For Pip Install
#curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && sudo python get-pip.py && sudo pip install flask && rm get-pip.py

from flask import Flask
from flask import render_template
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run()
