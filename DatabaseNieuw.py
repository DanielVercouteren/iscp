# -*- coding: utf-8 -*-
### Author: Daniël Vercouteren

import sqlite3 as lite

dbConn = lite.connect('tweets.db')
cur = dbConn.cursor()

def createTweetsDatabase():
    cur.execute("DROP TABLE IF EXISTS tweets")
    cur.execute("CREATE TABLE tweets (id INTEGER PRIMARY KEY AUTOINCREMENT, tweet TEXT, user TEXT, date DATE, score INT)")
    dbConn.commit()
    print("Nieuwe tabel tweets gecreëerd.")

def setTweetsDatabase(tweet, user, date):
    cur.execute("INSERT INTO tweets (tweet, user, date) VALUES (?,?,?)", (tweet, user, date))
    dbConn.commit()
    print("Tweet %s toegevoegd"% getAantalTweets())

def getTweets():
    cur.execute("SELECT tweet from tweets")
    tweetLijst = cur.fetchall()
    return tweetLijst

def setAnalysis(id, analyse):
    cur.execute("UPDATE tweets SET score = ? WHERE id = ?" , (analyse, id))
    dbConn.commit()

def getAnalysis():
    cur.execute("SELECT COUNT(score) FROM tweets WHERE score = 0")
    negatieve_woorden = cur.fetchone()[0]
    cur.execute("SELECT COUNT(score) FROM tweets WHERE score = 1")
    neutrale_woorden = cur.fetchone()[0]
    cur.execute("SELECT COUNT(score) FROM tweets WHERE score = 2")
    positieve_woorden = cur.fetchone()[0]

    analyseLijst = [negatieve_woorden, neutrale_woorden, positieve_woorden]
    return analyseLijst

def getAantalTweets():
    cur.execute("SELECT COUNT(tweet) FROM tweets")
    aantalTweets = cur.fetchone()[0]
    return aantalTweets

def getTimeChart():
    cur.execute("SELECT date, score FROM tweets ORDER BY date ASC")
    data = (cur.fetchall())
    return data