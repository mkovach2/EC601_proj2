<<<<<<< HEAD
# -*- coding: utf-8 -*-
'''
comnbined.py
Author: Miles Kovach
Created: 2020-09-27
Modified: 2020-09-28
EC601 Assignment 2

This script uses bits from each of the other modules, test_of_googleNLP
and test_of_tweepy.
'''

debug_mode = []

import test_of_tweepy as tot
import test_of_googleNLP as gnlp

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    print(allUsers[i], '\t\t', allSentiments[i])
  
if __name__ == '__main__':
=======
# -*- coding: utf-8 -*-
'''
comnbined.py
Author: Miles Kovach
Created: 2020-09-27
Modified: 2020-09-28
EC601 Assignment 2

This script uses bits from each of the other modules, test_of_googleNLP
and test_of_tweepy.
'''

debug_mode = []

import test_of_tweepy as tot
import test_of_googleNLP as gnlp

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
    print(allUsers[i], '\t\t', allSentiments[i])
  
if __name__ == '__main__':
>>>>>>> 484f19e39b931ca2e023fa908173b63f27a4b620
  main()