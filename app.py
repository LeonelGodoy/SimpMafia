from flask import Flask, render_template
import os
import requests

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    client_id = os.environ['MY_SECRET_SAUCE']
    client_secret = os.environ['MY_SECRET_ID']
    headers = {
        'Client-ID': client_id,
        'client_secret': client_secret,
        "grant_type": 'client_credentials',
        'Authorization': 'Bearer ' + os.environ['MY_SECRET_TOKEN']
    }
    streamers = ['cm_nyc_tv', 'gamerpool474_ph', 'snoozefighting', 'scentless__apprentice', 'mattnguyen', 'leyopan']
    dicts = {}
    for streamer in streamers:
        url = "https://api.twitch.tv/helix/streams?user_login=" + streamer

        response = requests.get(url, headers=headers).json()
        # data output
        dicts[streamer] = len(response['data'])

    return render_template("index.html", dicts=dicts)


if __name__ == '__main__':
    app.run()
