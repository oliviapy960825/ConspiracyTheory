#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:21:10 2020

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
from time import sleep


filename="combined_unique_tweeter_df_by_user_name"
infile = open(filename,'rb')
tweeting_df = pickle.load(infile)
infile.close()
print(tweeting_df)



tweeter_sample_by_num_of_status=tweeting_df.name.tolist()[5001:8001]

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
}


def expand_url(url):
#for i in range(len(url_mentioned)):
    if url not in already_expanded_url:
        session = requests.Session()
        try:
            r = session.head(url, allow_redirects=True, timeout=10, headers=headers)
            print(r.url)
            if r.url!=None and r.url not in expanded_url_list:
                expanded_url_list.append(r.url)
                already_expanded_url.append(url)
                #url_starter_unique_list.append(url_starter_list[i])
                return r.url
        except requests.Timeout:
            session = requests.Session()
        except requests.exceptions.ConnectionError:
            print("Connection refused")
            already_expanded_url.append(url)
        except:
            print("some kind of exceptions happened")
            already_expanded_url.append(url)
            
def get_urls(file,user):
    url_list=[]
    with open(file) as f:
         for line in f: 
                if json.loads(line)['lang']=='en' and json.loads(line)['user']['screen_name']==user:
                    if(len(json.loads(line)['entities'].get('urls'))>0):
                        for j in range(len(json.loads(line)['entities'].get('urls'))):
                            url=json.loads(line)['entities'].get('urls')[j].get('expanded_url')
                            print(url)
                            if expand_url(url)!=None:
                                print("appending"+url)
                                url_list.append(url)
    return url_list

"""
filename="suspended_account_index_list_for_sample"
infile = open(filename,'rb')
suspended_account_index_list = pickle.load(infile)
infile.close()
print(suspended_account_index_list)

suspended_account_url_list=[]
for index in suspended_account_index_list:
    user=tweeter_sample_by_num_of_status[index]
    print(user)
    expanded_url_list=[]
    already_expanded_url=[]
    url_list_1=get_urls("ae832c68a41b48b890a426e159076a9b_001.json",user)
    url_list_2=get_urls("ae832c68a41b48b890a426e159076a9b_002.json",user)
    url_list_3=get_urls("ae832c68a41b48b890a426e159076a9b_003.json",user)
    url_list_4=get_urls("ae832c68a41b48b890a426e159076a9b_004.json",user)
    suspended_account_url_list.append(url_list_1+url_list_2+url_list_3+url_list_4)
    
print(suspended_account_url_list)
flat_list = [item for sublist in suspended_account_url_list for item in sublist]
print(flat_list)

filename = 'url_list_for_suspended_accounts_to_2000'
outfile = open(filename,'wb')
pickle.dump(suspended_account_url_list,outfile)
outfile.close()

filename="bot_account_index_list_for_sample" #0-2000
infile = open(filename,'rb')
bot_account_index_list = pickle.load(infile)
infile.close()

bot_account_index_list=bot_index_list
print(bot_account_index_list)

bot_account_url_list=[]
for index in bot_account_index_list:
    user=tweeter_sample_by_num_of_status[index]
    print(user)
    expanded_url_list=[]
    already_expanded_url=[]
    url_list_1=get_urls("ae832c68a41b48b890a426e159076a9b_001.json",user)
    url_list_2=get_urls("ae832c68a41b48b890a426e159076a9b_002.json",user)
    url_list_3=get_urls("ae832c68a41b48b890a426e159076a9b_003.json",user)
    url_list_4=get_urls("ae832c68a41b48b890a426e159076a9b_004.json",user)
    bot_account_url_list.append(url_list_1+url_list_2+url_list_3+url_list_4)
    
print(bot_account_url_list)
filename = 'url_list_for_bots_5000_to_8000'
outfile = open(filename,'wb')
pickle.dump(bot_account_url_list,outfile)
outfile.close()
flat_list = [item for sublist in bot_account_url_list for item in sublist]
print(flat_list)

"""
print(len(flat_list))
"""
filename="human_account_index_list_for_sample" #0-2000
infile = open(filename,'rb')
human_account_index_list = pickle.load(infile)
infile.close()
print(human_account_index_list)

human_account_url_list=[]
for index in human_account_index_list:
    user=tweeter_sample_by_num_of_status[index]
    print(user)
    expanded_url_list=[]
    already_expanded_url=[]
    url_list_1=get_urls("ae832c68a41b48b890a426e159076a9b_001.json",user)
    url_list_2=get_urls("ae832c68a41b48b890a426e159076a9b_002.json",user)
    url_list_3=get_urls("ae832c68a41b48b890a426e159076a9b_003.json",user)
    url_list_4=get_urls("ae832c68a41b48b890a426e159076a9b_004.json",user)
    human_account_url_list.append(url_list_1+url_list_2+url_list_3+url_list_4)
    


#in_between_account_index_list_for_sample
filename="in_between_account_index_list_for_sample" #0-2000
infile = open(filename,'rb')
in_between_account_index_list = pickle.load(infile)
infile.close()
print(in_between_account_index_list)
in_between_account_url_list=[]
for index in in_between_account_index_list:
    user=tweeter_sample_by_num_of_status[index]
    print(user)
    expanded_url_list=[]
    already_expanded_url=[]
    url_list_1=get_urls("ae832c68a41b48b890a426e159076a9b_001.json",user)
    url_list_2=get_urls("ae832c68a41b48b890a426e159076a9b_002.json",user)
    url_list_3=get_urls("ae832c68a41b48b890a426e159076a9b_003.json",user)
    url_list_4=get_urls("ae832c68a41b48b890a426e159076a9b_004.json",user)
    in_between_account_url_list.append(url_list_1+url_list_2+url_list_3+url_list_4)

print(in_between_account_url_list)


filename="bot_account_index_list_for_sample_2001_to_5000" #2001-5000
infile = open(filename,'rb')
bot_account_index_list_2000_to_5000 = pickle.load(infile)
infile.close()

bot_account_url_list_2000_to_5000=[]
for index in bot_account_index_list_2000_to_5000:
    user=tweeter_sample_by_num_of_status[index]
    print(user)
    expanded_url_list=[]
    already_expanded_url=[]
    url_list_1=get_urls("ae832c68a41b48b890a426e159076a9b_001.json",user)
    url_list_2=get_urls("ae832c68a41b48b890a426e159076a9b_002.json",user)
    url_list_3=get_urls("ae832c68a41b48b890a426e159076a9b_003.json",user)
    url_list_4=get_urls("ae832c68a41b48b890a426e159076a9b_004.json",user)
    bot_account_url_list_2000_to_5000.append(url_list_1+url_list_2+url_list_3+url_list_4)

print(bot_account_url_list_2000_to_5000)
"""
"""
filename = 'url_list_for_bot_2000_to_5000'
outfile = open(filename,'wb')
pickle.dump(bot_account_url_list_2000_to_5000,outfile)
outfile.close()
flat_list = [item for sublist in bot_account_url_list_2000_to_5000 for item in sublist]
print(flat_list)

filename="url_list_for_bots_to_2000" #0-2000
infile = open(filename,'rb')
bot_account_url_list = pickle.load(infile)
infile.close()
print(bot_account_url_list)
flat_list = [item for sublist in bot_account_url_list for item in sublist]
print(flat_list)
"""
