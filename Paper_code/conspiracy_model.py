#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:55:18 2020

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
#punc_word=set(punctuation)
#stop_word=set(stopwords.words("English"))
#initiallist=""
#cleanlist = []
def read_and_process(file_name):
    df=pd.read_json(file_name, lines=True)
    columns=['coordinates', 'created_at',
       'entities', 'extended_entities', 'favorite_count', 'favorited',
       'full_text', 'id_str', 'in_reply_to_screen_name',
        'in_reply_to_status_id_str','in_reply_to_user_id_str',
       'lang', 'metadata', 'place', 'possibly_sensitive', 'quoted_status',
       'quoted_status_id_str', 'retweet_count',
       'retweeted', 'retweeted_status', 'source', 'truncated', 'user',
       ]
    ex_df=df[columns]
    ex_df=ex_df[ex_df['lang']=='en']
    return ex_df

#ex_df=read_and_process("ae832c68a41b48b890a426e159076a9b_005.json")
#print(ex_df)

df_1=read_and_process("ae832c68a41b48b890a426e159076a9b_001.json")
df_2=read_and_process("ae832c68a41b48b890a426e159076a9b_002.json")
df_3=read_and_process("ae832c68a41b48b890a426e159076a9b_003.json")
df_4=read_and_process("ae832c68a41b48b890a426e159076a9b_004.json")
df_5=read_and_process("ae832c68a41b48b890a426e159076a9b_005.json")
ex_df=df_1.append(df_2,ignore_index=True)
ex_df=ex_df.append(df_3,ignore_index=True)
dex_f=ex_df.append(df_4,ignore_index=True)
ex_df=ex_df.append(df_5,ignore_index=True)
print(ex_df)
