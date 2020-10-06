# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:10:06 2020

@author: miles_kovach
"""

import tweepy
import configparser
import pandas as pd

confKeys = configparser.ConfigParser(interpolation=None)

debug_mode = []

# reading keys from authentication from an authentication file called
# important.ini.  see iniTemplate.txt for how to format this.
confKeys.read('important.ini')
keyDict = confKeys['authentication_info']

auth = tweepy.OAuthHandler(keyDict['api_key'], keyDict['api_secret'])
auth.set_access_token(keyDict['access_token'], keyDict['access_secret'])

api = tweepy.API(auth, wait_on_rate_limit=False)

def myOwnLast(numTweets): # function that prints the most recent numTweet...
                          # ... tweets from one's own feed
  public_tweets = api.home_timeline()
  if 1 in debug_mode:
    for tweet in public_tweets[:numTweets]:
      print(tweet.author.screen_name, '\t', tweet.created_at, '\n', tweet.text, '\n')
    
  return public_tweets[:numTweets]
    
def searchShortcut(term, num):
  allDims = pd.DataFrame(columns  = ['id','lat','long','text'])
  while len(allDims.index) < num:
    j = api.search(q = term, count = num, result_type = 'recent', lang = 'en')
    for w in j:
      if (w.place != None) and not(w.id in allDims[['id']].values):
        wlat = w.place.bounding_box.coordinates[0][1][1]
        wlong = w.place.bounding_box.coordinates[0][1][0]
        allDims = allDims.append({'id':w.id,'lat':wlat, 'long':wlong, 'text':w.text}, ignore_index = 1)
  return(allDims)

def main():
  myOwnLast(19)
  bigMatrix = searchShortcut('a',10)
  print(bigMatrix)
  
if __name__ == '__main__':
  main()