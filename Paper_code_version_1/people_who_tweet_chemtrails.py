#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:30:59 2020

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


#analyze the bot score of the list of people tweeting chemtrails

"""def read_and_process_tweeter(file_name):
     #unique_tweeter_list=[]
     #follower_num_list=[]
     #friends_num_list=[]
     #status_num_list=[]
     tweeter_dictionary={}
     with open(file_name) as f:
         for line in f:
             if json.loads(line)['lang']=='en':
                 user_info=json.loads(line)['user']
                 tweeter_name=user_info['screen_name']
                 follower_num=user_info['followers_count']
                 friends_num=user_info['friends_count']
                 status_num=user_info['statuses_count']
                 if tweeter_name not in tweeter_dictionary:
                     #unique_tweeter_list.append(tweeter_name)
                     #follower_num_list.append(follower_num)
                     #friends_num_list.append(friends_num)
                     #status_num_list.append(status_num)
                     tweeter_dictionary[tweeter_name]={'follower_num':follower_num,'friends_num':friends_num,'status_num':status_num}
            #data.append(json.loads(line))
    
     #return unique_tweeter_list,follower_num_list,friends_num_list,status_num_list;
     return tweeter_dictionary
"""

"""tweeter_1_unique_tweeter_list,tweeter_1_follower_num_list,tweeter_1_friends_num_list,tweeter_1_status_num_list =read_and_process_tweeter("ae832c68a41b48b890a426e159076a9b_001.json")
tweeter_2_unique_tweeter_list,tweeter_2_follower_num_list,tweeter_2_friends_num_list,tweeter_2_status_num_list=read_and_process_tweeter("ae832c68a41b48b890a426e159076a9b_002.json")
tweeter_3_unique_tweeter_list,tweeter_3_follower_num_list,tweeter_3_friends_num_list,tweeter_3_status_num_list=read_and_process_tweeter("ae832c68a41b48b890a426e159076a9b_003.json")
tweeter_4_unique_tweeter_list,tweeter_4_follower_num_list,tweeter_4_friends_num_list,tweeter_4_status_num_list=read_and_process_tweeter("ae832c68a41b48b890a426e159076a9b_004.json")
"""
"""
tweeter_dict1=read_and_process_tweeter("ae832c68a41b48b890a426e159076a9b_001.json")
tweeter_dict2=read_and_process_tweeter("ae832c68a41b48b890a426e159076a9b_002.json")
tweeter_dict3=read_and_process_tweeter("ae832c68a41b48b890a426e159076a9b_003.json")
tweeter_dict4=read_and_process_tweeter("ae832c68a41b48b890a426e159076a9b_004.json")"""

#unique_tweeter_list=list(tweeter_dict1.keys())+list(tweeter_dict2.keys())+list(tweeter_dict3.keys())+list(tweeter_dict4.keys())
#print (unique_tweeter_list)
unique_tweeter_set=set(unique_tweeter_list)
print(unique_tweeter_set)

follower_num_list=[]
friends_num_list=[]
status_num_list=[]
for user in unique_tweeter_set:
    follower_num=0
    friends_num=0
    status_num=0
    if user in tweeter_dict1:
        follower_num=tweeter_dict1[user]['follower_num']
        friends_num=tweeter_dict1[user]['friends_num']
        status_num=tweeter_dict1[user]['status_num']
    if user in tweeter_dict2:
        follower_num=tweeter_dict2[user]['follower_num']
        friends_num=tweeter_dict2[user]['friends_num']
        status_num=tweeter_dict2[user]['status_num']
    if user in tweeter_dict3:
        follower_num=tweeter_dict3[user]['follower_num']
        friends_num=tweeter_dict3[user]['friends_num']
        status_num=tweeter_dict3[user]['status_num']
    if user in tweeter_dict4:
        follower_num=tweeter_dict4[user]['follower_num']
        friends_num=tweeter_dict4[user]['friends_num']
        status_num=tweeter_dict4[user]['status_num']
    follower_num_list.append(follower_num)
    friends_num_list.append(friends_num)
    status_num_list.append(status_num)
    
#full_text_5=read_and_process("ae832c68a41b48b890a426e159076a9b_005.json")
"""
unique_tweeter_list=tweeter_1_unique_tweeter_list+tweeter_2_unique_tweeter_list+tweeter_3_unique_tweeter_list+tweeter_4_unique_tweeter_list
follower_num_list=tweeter_1_follower_num_list+tweeter_2_follower_num_list+tweeter_3_follower_num_list+tweeter_4_follower_num_list
friends_num_list=tweeter_1_friends_num_list+tweeter_2_friends_num_list+tweeter_3_friends_num_list+tweeter_4_friends_num_list
status_num_list=tweeter_1_status_num_list+tweeter_2_status_num_list+tweeter_3_status_num_list+tweeter_4_status_num_list


chemtrail_freq=[]
chem_trail_tweets=[]
def get_num_chemtrail_tweets(file_name,user):
    with open(file_name) as f:
        chemtrail_tweets=[]
        chemtrail_num=0
        for line in f:
            if json.loads(line)['lang']=='en':
                text=json.loads(line)['full_text']
                user_name=json.loads(line)['user']['name']
                if user_name==user:
                    chemtrail_tweets.append(text)
                    chemtrail_num+=1
    return chemtrail_tweets,chemtrail_num

for user in unique_tweeter_list:
    chemtrail_tweets_1,chemtrail_num_1=get_num_chemtrail_tweets("ae832c68a41b48b890a426e159076a9b_001.json",user)
    chemtrail_tweets_2,chemtrail_num_2=get_num_chemtrail_tweets("ae832c68a41b48b890a426e159076a9b_002.json",user)
    chemtrail_tweets_3,chemtrail_num_3=get_num_chemtrail_tweets("ae832c68a41b48b890a426e159076a9b_003.json",user)
    chemtrail_tweets_4,chemtrail_num_4=get_num_chemtrail_tweets("ae832c68a41b48b890a426e159076a9b_004.json",user)
    #chemtrail_num=get_num_chemtrail_tweets("ae832c68a41b48b890a426e159076a9b_001.json",user).chemtrail_num+get_num_chemtrail_tweets("ae832c68a41b48b890a426e159076a9b_002.json",user).chemtrail_num+get_num_chemtrail_tweets("ae832c68a41b48b890a426e159076a9b_003.json",user).chemtrail_num+get_num_chemtrail_tweets("ae832c68a41b48b890a426e159076a9b_004.json",user).chemtrail_num
    
    chemtrail_freq.append(chemtrail_tweets_1+chemtrail_tweets_2+chemtrail_tweets_3+chemtrail_tweets_4)
    chem_trail_tweets.append(chemtrail_num_1+chemtrail_num_2+chemtrail_num_3+chemtrail_num_4)
    


tweeting_df=pd.DataFrame(list(zip(unique_tweeter_list, follower_num_list, friends_num_list,status_num_list)), #add chemtrail_freq to get the frequency 
                 columns =['name','num_follower','num_friends','total_status_num']) 
tweeting_df=tweeting_df[tweeting_df['total_status_num']!=0]
#tweeting_df['tweeting_chemtrail_fre']=tweeting_df.apply(lambda row: row.number_of_tweets_about_chemtrail / row.num_tweeting, axis=1)
#tweeting_df=tweeting_df.sort_values(by='num_tweeting', ascending=False)

tweeting_df=tweeting_df.sort_values(by='total_status_num', ascending=False)
print(tweeting_df)


filename = 'unique_tweeter' # user's twitter name, not twitter handle
outfile = open(filename,'wb')
pickle.dump(unique_tweeter_list,outfile)
outfile.close()

filename = 'unique_tweeter_num_follower'
outfile = open(filename,'wb')
pickle.dump(follower_num_list,outfile)
outfile.close()

filename = 'unique_tweeter_num_friends'
outfile = open(filename,'wb')
pickle.dump(friends_num_list,outfile)
outfile.close()

filename = 'unique_tweeter_total_status_num'
outfile = open(filename,'wb')
pickle.dump(status_num_list,outfile)
outfile.close()


filename = 'unique_tweeter_df'
outfile = open(filename,'wb')
pickle.dump(tweeting_df,outfile)
outfile.close()   

filename = 'unique_tweeter_user_name'
outfile = open(filename,'wb')
pickle.dump(unique_tweeter_list,outfile)
outfile.close()

filename = 'unique_tweeter_num_follower_by_user_name'
outfile = open(filename,'wb')
pickle.dump(follower_num_list,outfile)
outfile.close()

filename = 'unique_tweeter_num_friends_by_user_name'
outfile = open(filename,'wb')
pickle.dump(friends_num_list,outfile)
outfile.close()

filename = 'unique_tweeter_total_status_num_by_user_name'
outfile = open(filename,'wb')
pickle.dump(status_num_list,outfile)
outfile.close()


filename = 'unique_tweeter_df_by_user_name'
outfile = open(filename,'wb')
pickle.dump(tweeting_df,outfile)
outfile.close() """ 