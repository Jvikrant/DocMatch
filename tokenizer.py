# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 17:06:48 2018

@author: jdhruwa
"""
################################################
#Read data from files (JD & exp_dataset)
# =============================================================================
# from fileRead import get_text
# path="..\JD & GuideLine\CG Evaluation Guidelines_ASP.NET MVC.PDF"
# fileContent=get_text(path)
# 
# import pandas as pd
# dataset=pd.read_csv("dataset.csv")
# =============================================================================
################################################

################################################
#To tokenize the dataset
# =============================================================================
# import spacy
# spacy.load('en_core_web_sm')
# from spacy.lang.en import English
# parser = English()
# def tokenize(text):
#     lda_tokens = []
#     tokens = parser(text)
#     for token in tokens:
#         if token.orth_.isspace():
#             continue
#         elif token.like_url:
#             lda_tokens.append('URL')
#         elif token.orth_.startswith('@'):
#             lda_tokens.append('SCREEN_NAME')
#         else:
#             lda_tokens.append(token.lower_)
#     return lda_tokens
# =============================================================================


# =============================================================================
# tokenList=[]
# for index, row in dataset.iterrows():
#    tokenList.extend(tokenize(row[0]))
#    
# tokenSet=list(set(tokenList))
# tokenSet.sort()
# =============================================================================
##################################################


##################################################
#Morphing & Lemmatization
import nltk
#nltk.download('wordnet')

from nltk.corpus import wordnet as wn
def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma

# =============================================================================
# morphList=[]
# for word in tokenSet:
#     morphList.append(get_lemma(word))
# =============================================================================

from nltk.stem.wordnet import WordNetLemmatizer
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

# =============================================================================
# morphList2=[]
# for word in tokenSet:
#     morphList2.append(get_lemma2(word))
# =============================================================================

################################################

################################################
#Filtering Stop words
#nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
en2=set(["ak","must","etc","skill","service","experience","good","yr","knowledge","framework","code","server","quality","technical","parameter","nice","good","etc."])
en_stop=en_stop.union(en2)

def prepare_text_for_lda(text):
    tokens = text.split(' ')
    tokens = [token for token in tokens if len(token) > 1]    
    tokens = [get_lemma(token) for token in tokens]
    tokens = [token for token in tokens if token not in en_stop]
    return tokens

