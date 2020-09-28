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

# debug block 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

client = language.LanguageServiceClient()

def text2doc(inStr):
  document = language.types.Document(
    content=inStr,
    language='en',
    type='PLAIN_TEXT',
  )
  return document

def analSent(inDoc):
  response = client.analyze_sentiment(
     document=text2doc(inDoc),
     encoding_type='UTF32',
  )
  
  sentiment = response.document_sentiment
  if 2 in debug_mode:
    print(sentiment.score)
  return sentiment.score

# debug block 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this part is from google
# https://googleapis.dev/python/language/latest/usage.html
  
def main():
  
  text2doc('Hi i am having a lot of fun!  :) whee.')
  
  #sentiment = response.document_sentiment
  #print(sentiment.score)
  
  # p = print_result(document)
  #return p
  #print_result('hi i am very happy!  wow!')
  
if __name__ == '__main__':
=======
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

# debug block 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

client = language.LanguageServiceClient()

def text2doc(inStr):
  document = language.types.Document(
    content=inStr,
    language='en',
    type='PLAIN_TEXT',
  )
  return document

def analSent(inDoc):
  response = client.analyze_sentiment(
     document=text2doc(inDoc),
     encoding_type='UTF32',
  )
  
  sentiment = response.document_sentiment
  if 2 in debug_mode:
    print(sentiment.score)
  return sentiment.score

# debug block 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this part is from google
# https://googleapis.dev/python/language/latest/usage.html
  
def main():
  
  text2doc('Hi i am having a lot of fun!  :) whee.')
  
  #sentiment = response.document_sentiment
  #print(sentiment.score)
  
  # p = print_result(document)
  #return p
  #print_result('hi i am very happy!  wow!')
  
if __name__ == '__main__':
>>>>>>> 484f19e39b931ca2e023fa908173b63f27a4b620
  main()