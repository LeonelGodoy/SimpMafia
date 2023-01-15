from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

import tweepy



@app.route('/')
def main():  # put application's code here
    bearer_token = os.environ['MY_BEARER_TOKEN']

    client_id = os.environ['MY_SECRET_SAUCE']
    client_secret = os.environ['MY_SECRET_ID']
    headers = {
        'Client-ID': client_id,
        'client_secret': client_secret,
        "grant_type": 'client_credentials',
        'Authorization': 'Bearer ' + os.environ['MY_SECRET_TOKEN']
    }
    streamers = ['cm_nyc_tv', 'gamerpool474_ph', 'snoozefighting', 'scentless__apprentice',
                 'mattnguyen', 'leyopan', 'camelul', 'replaisment']
    dicts = {}
    for streamer in streamers:
        url = "https://api.twitch.tv/helix/streams?user_login=" + streamer

        response = requests.get(url, headers=headers).json()
        # data output
        dicts[streamer] = len(response['data'])

    client = tweepy.Client(bearer_token=bearer_token)
    cm_tweet = client.get_users_tweets(id='930662549812600832')
    tweet1 = cm_tweet[0][0].id
    tweet2 = cm_tweet[0][1].id
    tweet3 = cm_tweet[0][2].id
    lilb_tweet = client.get_users_tweets(id='37836873')
    tweet4 = lilb_tweet[0][0].id
    jennie_tweet = client.get_users_tweets(id='3243685400')
    tweet5 = jennie_tweet[0][0].id

    return render_template("index.html", dicts=dicts,
                           tweet1=tweet1, tweet2=tweet2, tweet3=tweet3, tweet4=tweet4, tweet5=tweet5)


if __name__ == '__main__':
    app.run()
