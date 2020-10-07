#-------10--------20--------30--------40--------50--------60--------70-------79

'''
README.txt
Author: Miles Kovach
Created: 2020-09-28
Modified: 2020-10-06
EC602 Assignment 2
'''

This is the beginnings to an app which has the ultimate goal of creating a map
with clusters based on sentiment surrounding a given term.  It will implement 
a k-means clustering algorithm (kmeans.py) to sort tweets collected by
test_of_tweepy.py based on the latitude and longitude attached to the tweet.

Totalprog.py is the main program to assemble all the components.

test_of_googleNLP.py is the connection to googles NLP service, allowing the
program to access the sentiment function.

User stories:
As a user, I want to know whether there are any location-base correlations
between the term i search for on twitter.
As a user, I want to have a gui that plots any clusters to a map (implement
later)
As a user, I might want to be able to sort by per-capita or absolute.

The typical user of this program, as it is, might just be a casual user who
wants to observe trends for fun.  A more developed version of this program
could appeal to an advertising audience, or a political audience to analyze
trends and attitudes about a subject of their choice.