from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    keys = {'MY_SECRET_SAUCE': 'onwbl5f7e4izyjd7h5x4yv8d4o6gat', 'MY_SECRET_ID': '0vx9sscucig7b24gyyrxjkjwj16azq'}
    return render_template("index.html", keys=keys)

if __name__ == '__main__':
    app.run()
