#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:26:48 2020

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
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#punc_word=set(punctuation)
#stop_word=set(stopwords.words("English"))
#initiallist=""
#cleanlist = []

all_full_text=[]
def read_and_process(file_name):
    full_text=[]
    with open(file_name) as f:
        for line in f:
            if json.loads(line)['lang']=='en':
                text=json.loads(line)['full_text']
                if (text.startswith("RT") and ('retweeted_status' in json.loads(line))):
                    full_text.append(json.loads(line)['retweeted_status']['full_text'])
                else:
                    full_text.append(json.loads(line)['full_text'])
            #data.append(json.loads(line))
    
    return full_text

#ex_df=read_and_process("ae832c68a41b48b890a426e159076a9b_005.json")
#print(ex_df)

full_text_1=read_and_process("ae832c68a41b48b890a426e159076a9b_001.json")
full_text_2=read_and_process("ae832c68a41b48b890a426e159076a9b_002.json")
full_text_3=read_and_process("ae832c68a41b48b890a426e159076a9b_003.json")
full_text_4=read_and_process("ae832c68a41b48b890a426e159076a9b_004.json")
#full_text_5=read_and_process("ae832c68a41b48b890a426e159076a9b_005.json")

#print(full_text_1)


full_text_list=full_text_1+full_text_2+full_text_3+full_text_4

filename = 'full_text_unprocessed' #pickle file's name is full_text_unprocessed
outfile = open(filename,'wb')
pickle.dump(full_text_list,outfile)
outfile.close()

pkl_lst = open('full_text_unprocessed', 'rb')
full_text_list=pickle.load(pkl_lst)

p.set_options(p.OPT.URL, p.OPT.EMOJI)
full_text_list_processed=[]
for x in range(len(full_text_list)):
    full_text=full_text_list[x]
    clean = re.compile('<.*?>')
    full_text_processed=re.sub(clean, '', full_text)
    full_text_processed=p.clean(full_text)
    full_text_processed=re.sub('[,\.!?]', '', full_text_processed)
    full_text_processed = re.sub(r'[^a-zA-Z0-9\s]', ' ', full_text_processed) 
    full_text_processed=full_text_processed.lower()
    full_text_processed = re.sub("#", "", full_text_processed)
    full_text_list_processed.append(full_text_processed)
# Convert the titles to lowercase
#full_text_list_processed = full_text_list_processed.apply(lambda x: x.lower())# Print out the first rows of papers
print(full_text_list_processed)

filename = 'full_text_processed' #pickle file's name is full_text_processed
outfile = open(filename,'wb')
pickle.dump(full_text_list_processed,outfile)
outfile.close()



punc_word=set(punctuation)
stop_word=set(stopwords.words("English"))
self_defined_stop_words={"chemtrail","chemtrails ","chemtrails","Chemtrail","Chemtrails","GeoEngineering","geoengineering","IDoNotConsent","WeDoNotConsent","stopsprayingus","amp","geoengineering","idonotconsent","us","people","like"}
new_stop_word=stop_word.union(punc_word,self_defined_stop_words)
sns.set_style('whitegrid')
#%matplotlib inline
# Helper function

def plot_30_most_common_ngrams(count_data, count_vectorizer):
    words = count_vectorizer.get_feature_names()
    total_counts = np.zeros(len(words))
    for t in count_data:
        total_counts+=t.toarray()[0]
    
    count_dict = (zip(words, total_counts))
    count_dict = sorted(count_dict, key=lambda x:x[1], reverse=True)[:30]
    words = [w[0] for w in count_dict]
    counts = [w[1] for w in count_dict]
    x_pos = np.arange(len(words)) 
    
    plt.figure(2, figsize=(15, 15/1.6180))
    plt.subplot(title='30 most common words')
    sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth": 2.5})
    sns.barplot(x_pos, counts, palette='husl')
    plt.xticks(x_pos, words, rotation=90) 
    plt.xlabel('words')
    plt.ylabel('counts')
    plt.show()# Initialise the count vectorizer with the English stop words
    
    
count_vectorizer = CountVectorizer(max_df=0.99,min_df=3,ngram_range=(1,1),stop_words=new_stop_word)# Fit and transform the processed titles
count_data = count_vectorizer.fit_transform(full_text_list_processed)# Visualise the 30 most common words
plot_30_most_common_ngrams(count_data, count_vectorizer)

count_vectorizer = CountVectorizer(max_df=0.99,min_df=3,ngram_range=(2,2),stop_words=new_stop_word)# Fit and transform the processed titles
count_data = count_vectorizer.fit_transform(full_text_list_processed)# Visualise the 30 most common words
plot_30_most_common_ngrams(count_data, count_vectorizer)



#print most common trigrams
count_vectorizer = CountVectorizer(max_df=0.99,min_df=3,ngram_range=(3,3),stop_words=new_stop_word)# Fit and transform the processed titles
count_data = count_vectorizer.fit_transform(full_text_list_processed)# Visualise the 30 most common words
plot_30_most_common_ngrams(count_data, count_vectorizer)


import warnings
warnings.simplefilter("ignore", DeprecationWarning)# Load the LDA model from sk-learn
#from sklearn.decomposition import LatentDirichletAllocation as LDA


import lda
# Helper function
def print_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print("\nTopic #%d:" % topic_idx)
        print(" ".join([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
        
# Tweak the two parameters below
number_topics = 20
number_words = 10# Create and fit the LDA model
lda = lda.LDA(n_topics=number_topics)
lda.fit(count_data)# Print the topics found by the LDA model
print("Topics found via LDA:")
print_topics(lda, count_vectorizer, number_words)

"""import pickle
filename = 'full_text_processed'
outfile = open(filename,'wb')
pickle.dump(full_text_processed,outfile)
outfile.close()"""
