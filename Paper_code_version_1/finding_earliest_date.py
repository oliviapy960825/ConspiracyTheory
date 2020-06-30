#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:22:29 2020

@author: wangpeiyu
"""
import pandas as pd
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
from datetime import datetime
#punc_word=set(punctuation)
#stop_word=set(stopwords.words("English"))
#initiallist=""
#cleanlist = []

def read_and_process(file_name):
    df=pd.read_json(file_name, lines=True)
    columns=['created_at','lang']
    ex_df=df[columns]
    ex_df=ex_df[ex_df['lang']=='en']
    return ex_df

#ex_df=read_and_process("ae832c68a41b48b890a426e159076a9b_005.json")
#print(ex_df)

#time_df_1=read_and_process("ae832c68a41b48b890a426e159076a9b_001.json")
print(time_df_1.dtypes)
print(time_df_1.created_at.min())
#time_df_1.created_at=time_df_1.created_at.astype(datetime)
#time_df_1_exp=pd.to_datetime(time_df_1, infer_datetime_format=True)  
#print(time_df_1_exp.dtypes)
#time_df_1=time_df_1.tz_convert(None)
#time_df_1.to_excel("chemtrail_time_1.xlsx")
time_df_5=read_and_process("ae832c68a41b48b890a426e159076a9b_005.json")
#time_df_5.to_excel("chemtrail_time_5.xlsx")
print(time_df_5.dtypes)
print(time_df_5.created_at.min())