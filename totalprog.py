# -*- coding: utf-8 -*-
'''
totalprog.py
Author: Miles Kovach
Created: 2020-10-06
Modified: 2020-10-06
EC601 Assignment 2

This script uses bits from each of the other modules, test_of_googleNLP
and test_of_tweepy.
'''

debug_mode = []

import pandas as pd
import test_of_tweepy as tot
import test_of_googleNLP as gnlp

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~

term = 'debug' # term to search for in later function
twtCount = 10 #number of tweets to retrieve in search

lastTweet = tot.myOwnLast(10)
allUsers = []
allTweets = []
allSentiments = []

if 1 in debug_mode:
  for tweetItem in lastTweet:
    print(tweetItem.text)

for tweetItem in lastTweet:
  allUsers.append(tweetItem.author.screen_name)
  allTweets.append(tweetItem.text)
  allSentiments.append(gnlp.analSent(tweetItem.text))
  
def main():
  for i in range(len(allTweets)):
    if 2 in debug_mode:
      print(allUsers[i], '\t\t', allSentiments[i])
    
  bigMatrix = pd.DataFrame()
  bigMatrix = tot.searchShortcut(term,twtCount)
  print(bigMatrix)
  for tweetText in bigMatrix[['text']].values:
    print(tweetText)
  
if __name__ == '__main__':
  main()
  
  
  
  
  
  
  
  
