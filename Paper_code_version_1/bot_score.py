#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 22:21:47 2020

@author: wangpeiyu
"""

import pandas as pd
import numpy as np
import requests
import nltk
import json
import random
from nltk import word_tokenize,sent_tokenize
import nltk
from nltk.corpus import state_union 
from nltk.collocations import *
import urllib.request
import pickle
from nltk.corpus import stopwords
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer
from time import sleep
import pickle
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
# Remove punctuation
import preprocessor as p
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import botometer
"""
filename="combined_unique_tweeter_df_by_user_name"
infile = open(filename,'rb')
tweeting_df = pickle.load(infile)
infile.close()
print(tweeting_df)

tweeter_by_num_of_status=tweeting_df.name.tolist()
tweeter_status_num_by_num_of_status=tweeting_df.total_status_num.tolist()
#print(tweeter_by_num_of_status)

#print(tweeter_status_num_by_num_of_status[50000])
#rapidapi_key = "a12f91f4e5msh2ac46e11516f060p113d24jsn794aef1651db"

tweeter_sample_by_num_of_status=tweeter_by_num_of_status[5001:8001]
tweeter_status_num_sample_by_num_of_status=tweeter_status_num_by_num_of_status[5001:8001]

rapidapi_key = "1d794e7532msh23d99165feb5188p1d8d51jsn78ff1d9f40f1"


twitter_app_auth = {
    'consumer_key': '5gLN744C9tUvWS8iwJmsyoVyV',
    'consumer_secret': 'C4HVb5qdKSEI64A4F94mqAoxDpCiRmmEsvgRStjbBaSeK8CS8w',
    'access_token': '1069716839440232448-hROnAYn4tXivcTkwIdNVuw7sNvVxE5',
    'access_token_secret': 'Sw66VM16tudODQm76wVyNl1OtAwwEHmbyL8rFvZzOrNc9',
  }

bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name

bot_score_list=[]
for index in range(len(tweeter_sample_by_num_of_status)):
    try:
        print(index)
        user=tweeter_sample_by_num_of_status[index]
        print(user)
        result = bom.check_account(user)['cap']['english']
    except Exception as e: 
        print(e)
        print("account suspended at index "+str(index))
        result=-1
    bot_score_list.append(result)
    
print(bot_score_list)
#print(result['cap']['english'])





filename = 'bot_score_list_for_sample_5001_to_8000'
outfile = open(filename,'wb')
pickle.dump(bot_score_list,outfile)
outfile.close()
"""
#count the number of suspended account

"""
suspended_account_list = [num if num == -1 else 0 for num in bot_score_list]
suspended_account_index_list=[i for i, elem in enumerate(bot_score_list) if elem==-1]
print(suspended_account_index_list)
print(len(suspended_account_index_list))
#print("The number of suspended account in the 50000 most tweeting accounts is: "+str(len(suspended_account_index_list)))

filename = 'suspended_account_index_list_for_sample_2001_to_5000'
outfile = open(filename,'wb')
pickle.dump(suspended_account_index_list,outfile)
outfile.close()
"""
##bot-- bot score>0.8
#bot_list=[num if num >=0.8 else 0 for num in bot_score_list]
bot_index_list=[i for i, elem in enumerate(bot_score_list) if elem>=0.8]
print(bot_index_list)
print("The number of suspected bots in the first 50000 most tweeting accounts is: "+str(len(bot_index_list)))

filename = 'bot_account_index_list_for_sample_5001_to_8000'
outfile = open(filename,'wb')
pickle.dump(bot_index_list,outfile)
outfile.close()
"""
##human -- bot score <0.2
#human_list=[num if (num < 0.2 and num >0) else 0 for num in bot_score_list]
human_index_list=[i for i, elem in enumerate(bot_score_list) if (elem<0.2 and elem>0)]
print(human_index_list)
print("The number of suspected human in the first 50000 most tweeting accounts is: "+str(len(human_index_list)))

filename = 'human_account_index_list_for_sample_2001_to_5000'
outfile = open(filename,'wb')
pickle.dump(human_index_list,outfile)
outfile.close()

##in-between
#in_between_list=[num if (num < 0.8 and num >0.2) else 0 for num in bot_score_list]

in_between_index_list=[i for i, elem in enumerate(bot_score_list) if (elem<0.8 and elem>0.2)]
print(in_between_index_list)
print("The number of in-between accounts in the first 50000 most tweeting accounts is: "+str(len(in_between_index_list)))
filename = 'in_between_account_index_list_for_sample_2001_to_5000'
outfile = open(filename,'wb')
pickle.dump(in_between_index_list,outfile)
outfile.close()
"""