#-------10--------20--------30--------40--------50--------60--------70-------79

'''
kmeans.py
Author: Miles Kovach
Created: 2020-10-06
Modified: 2020-10-06
EC601 Assignment 2

this takes in a pandas dataframe with columns 'lat' 'long' and 'sentiment,'
and computes K centroids, which it returns along with the total sentiment
contained within those centroids.
'''

import pandas as pd
import numpy as np

debug_mode = [0]

# debug block 0 ~~~~~~~~~~~~~~~~~~~~~~~~
if 0 in debug_mode:
  demoDf = pd.DataFrame(np.random.randint(0, 5, size=(9,3)), columns=['lat', 'long', 'sentiment'])

k = 2 # how many centroids to set

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~

def kmeans(inDf):
  Jold = 10000 # starter value for j
  costJ = 0 # this is going to need to be modified to account for spherical shape of earth.
  centroids = pd.DataFrame()
  # whoops this is a little incomplete
  while (costJ - Jold) > 0.0001:
    costJ = 
  return inDf

def main():
  if 0 in debug_mode:
    print(kmeans(demoDf))

if __name__ == '__main__':
  main()