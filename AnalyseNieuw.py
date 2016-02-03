# -*- coding: utf-8 -*-
### Author: Daniël Vercouteren

import sys
import Woordenlijst
import DatabaseNieuw
import InterfaceNieuw

def startAnalyse():
    tweetNummer = 0
    tweetLijst = DatabaseNieuw.getTweets()
    for tweet in tweetLijst:
        tweetNummer += 1
        analyse(tweet, tweetNummer)

def analyse(tw, tweetNummer):
    #Tuple naar string
    tweet = "".join(tw)
    print(tweet)

    #Set score op 0
    score = 0

    for tweetWoord in tweet.split():
        for analyseWoord in Woordenlijst.negatieveWoorden:
            #als woord gelijk is aan negatief woord, haal 1 punt van de score af
            if tweetWoord == analyseWoord:
                score -= 1
        for analyseWoord in Woordenlijst.positieveWoorden:
            #als woord gelijk is aan negatief woord, voeg 1 punt aan de score toe
            if tweetWoord == analyseWoord:
                score += 1

    scoring(score, tweetNummer)

def scoring(tweetScore, tweetNummer):
    print("Dit is tweet #" + str(tweetNummer))
    sys.stdout.write("Deze tweet is: ")
    if tweetScore > 0:
        print("positief")
        DatabaseNieuw.setAnalysis(tweetNummer, '2')

    elif tweetScore < 0:
        print("negatief")
        DatabaseNieuw.setAnalysis(tweetNummer, '0')

    else:
        print("neutraal")
        DatabaseNieuw.setAnalysis(tweetNummer, '1')

