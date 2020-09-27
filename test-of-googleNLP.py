# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:01:15 2020

@author: miles_kovach

based on instructions from youtube user sentdex
https://www.youtube.com/watch?v=-13yIXiyFAs
Natural Language API - Google Cloud Python Tutorials p.4
"""

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
#from sys import argv
#import json
import os

debug_mode = [] # list of debug blocks in which debug_mode will be on

# debug block 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
  r'C:\Users\miles_kovach\Documents\EC601\proj_2\EC601-2-f7721bcfe7f6.json'
if 1 in debug_mode:
  print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

def language_analysis(text):
  client = language.LanguageServiceClient()
  #client2 = language.Client()
#  document = client.document_from_text(text)
#  sent_analysis = document.analyze_sentiment()
#  print(dir(sent_analysis))
  
def main():
 p = language_analysis('hi i am very happy!  wow!')
 print(p)
  
if __name__ == '__main__':
  main()