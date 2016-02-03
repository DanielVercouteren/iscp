# -*- coding: utf-8 -*-
### Author: Daniël Vercouteren

import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import DatabaseNieuw
import AnalyseNieuw
import datetime

#Consumer key en secret
ckey = 'J4yO9TWts41BJBsUWBblODtUx'
csecret = 'Z0mscn8TlFGrBpJPV49taibhfPwVhEh14a3MZalweRiIH878Di'
#Access token en token secret
atoken = '25962657-MjKSNGIJdZHSd8n7c0rEZEwrybw38wSYnGxCOeQTR'
asecret = 'YbjOiggQ1RbD6acvLaFsZhWoBJ4riNnsYwTxAKUMMpUoL'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

#Aantal te behandelen tweets + filter
filter = 'Trump'
aantalTweets = 10000

class MyListener(StreamListener):
    def on_data(self, data):
        fullData = json.loads(data)
        try:
            #Controleer aantal tweets in db en max aantal tweets
            if DatabaseNieuw.getAantalTweets() != aantalTweets:
                #data maken en filteren
                timestamp = fullData['timestamp_ms']
                tweet = fullData['text']
                userData = fullData['user']
                user = userData['screen_name']

                #Mentions en Retweets uitsluiten
                if tweet.startswith("RT @") or tweet.startswith("@"):
                    return True
                if '"' in tweet:
                    tweet.replace('"', '')
                if '"' in user:
                    user.replace('"', '')

                #plaats data in de db
                DatabaseNieuw.setTweetsDatabase(tweet, user, timestamp)
            else:
                #Max aantal tweets is bereikt, doe analyse en stop daarna.
                AnalyseNieuw.startAnalyse()
                return False

        except KeyError:
            return True

    def on_error(self, status):
        print(status)
        return False

twitterStream = Stream(auth, MyListener())
twitterStream.filter( track=[filter], encoding='utf8', languages=['en'])
