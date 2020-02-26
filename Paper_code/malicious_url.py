#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:42:08 2020

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
import tldextract


"""
filename="url_list_for_suspended_accounts_to_2000" #0-2000
infile = open(filename,'rb')
suspended_account_url_list = pickle.load(infile)
infile.close()
print(suspended_account_url_list)
flat_list = [item for sublist in suspended_account_url_list for item in sublist]
print(flat_list)

filename="url_list_for_in_between_to_2000" #0-2000
infile = open(filename,'rb')
in_between_account_url_list = pickle.load(infile)
infile.close()
print(in_between_account_url_list)
flat_list = [item for sublist in in_between_account_url_list for item in sublist]
print(flat_list)


filename="url_list_for_human_to_1588" #0-2000
infile = open(filename,'rb')
human_account_url_list = pickle.load(infile)
infile.close()
print(human_account_url_list)
flat_list = [item for sublist in human_account_url_list for item in sublist]
print(flat_list)

scanned_list=[]
malicious_url=[]
not_avail_list=[]

#api_key='8d7185168f9d1b8241fdee1c5729a248562503d49783ea10cfce995acf58186a'
api_key='a8c31f6b781aca5615f299b85de9147b4415537984a06eaf5b7bbfb1376ca2bf'
for url in flat_list:
    if url not in scanned_list:
        print(url)
        input_url = 'https://www.virustotal.com/vtapi/v2/url/scan'
        params = {'apikey': 'a8c31f6b781aca5615f299b85de9147b4415537984a06eaf5b7bbfb1376ca2bf', 'url':url}
        response = requests.post(input_url, data=params)
       
        print(response)
        #print(response.json())
        if response.status_code==200 and len(response.json())>0 and response.json()['response_code']==1:
            print("response code 200")
            scanned_list.append(url)
            scan_id = response.json()['scan_id']
            sleep(15)
                    #results_file = open('VirusTotal Labels/1pct_results_expanded.txt','a+')
            input_url = 'https://www.virustotal.com/vtapi/v2/url/report'
            try:
                params = {'apikey': api_key, 'resource':scan_id}
                response = requests.get(input_url, params=params)
                print(response)
                print(response.json())
                #results_file.write(str(response.json())+'\n')
                
                if response.json()['positives']>0:
                    malicious_url.append(url)
            except:
                print("error")
                not_avail_list.append(url)
                        #results_file.write('Error in URL: ' + url_scan + 'with scan ID: ' + str(scan_id)+'\n')
            #results_file.close()
        sleep(15)
print(malicious_url)


filename = 'malicious_url_list_for_bots_5000_to_8000'
outfile = open(filename,'wb')
pickle.dump(malicious_url,outfile)
outfile.close()

"""

expanded_malicious_url_list=[]
already_expanded_url=[]
def expand_url(url):
#for i in range(len(url_mentioned)):
    if url not in already_expanded_url:
        session = requests.Session()
        try:
            r = session.head(url, allow_redirects=True, timeout=10, headers=headers)
            print(r.url)
            if r.url!=None and r.url not in expanded_malicious_url_list:
                expanded_malicious_url_list.append(r.url)
                already_expanded_url.append(url)
                #url_starter_unique_list.append(url_starter_list[i])
                #return r.url
        except requests.Timeout:
            session = requests.Session()
        except requests.exceptions.ConnectionError:
            print("Connection refused")
            already_expanded_url.append(url)
        except:
            print("some kind of exceptions happened")
            already_expanded_url.append(url)

for url in malicious_url:
    expand_url(url)
    #expanded_malicious_url_list.append(expand_url(url))

print(expanded_malicious_url_list)

malicious_top_domain={}

for url in expanded_malicious_url_list:
    top_domain=tldextract.extract(url).domain
    if top_domain not in malicious_top_domain:
        malicious_top_domain[top_domain]=1
    else:
        malicious_top_domain[top_domain]+=1
print(malicious_top_domain)

"""
filename = 'malicious_top_domains_for_human_to_2000'
outfile = open(filename,'wb')
pickle.dump(malicious_top_domain,outfile)
outfile.close()
"""