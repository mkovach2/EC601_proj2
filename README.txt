#-------10--------20--------30--------40--------50--------60--------70-------79

'''
README.txt
Author: Miles Kovach
Created: 2020-09-28
Modified: 2020-09-28
EC602 Assignment 2
'''

This project, as of 2020-09-28, is a simple exercise of the Twitter API and
the Google natural language processing API.

Its main file, "comnbined.py" takes a number of most recent tweets in a user's
own twitter feed and uses Google's NLP to analyze each of them.  The output
is a simple table of twitter handles paired with the tweet's respective
sentiment score.

Potential next steps:
- apply this to the general feed, rather than just the user's own feed.
- implement more mathematics as options- averaging across username or hashtag
  I'll almost definitely get NumPy involved somewhere in here.
- implement geographical analysis, and track different sentimential reactions
  across regions.
