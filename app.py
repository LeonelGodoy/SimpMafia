from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    print(os.environ['MY_SECRET_SAUCE'])
    keys = {'MY_SECRET_SAUCE': os.environ['MY_SECRET_SAUCE'], 'MY_SECRET_ID': os.environ['MY_SECRET_SAUCE']}
    return render_template("index.html", keys=keys)

if __name__ == '__main__':
    print(os.environ['MY_SECRET_SAUCE'])
    app.run()
