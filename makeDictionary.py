# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:48:43 2018

@author: jdhruwa
"""
# =============================================================================
# 
#from fileRead import get_text 
#path="..\JD & GuideLine\CG Evaluation Guidelines_ASP.NET MVC.PDF"
#fileContent=get_text(path)
# 
# import pandas as pd
# dataset=pd.read_csv("dataset.csv")
# =============================================================================
from fileRead import get_text
txtfile=[txt for txt in get_text("JD & GuideLine\CG Evaluation Guidelines_ASP.NET MVC.PDF").split('\n')]
#txtfile=[txt for txt in get_text("..\JD & GuideLine\JD - ADM Practice - .NET WPF Developer.docx").split('\n')]

#Text extracted from dataset/file
#import random
from tokenizer import prepare_text_for_lda
text_data = []
# =============================================================================
# with open('dataset.csv') as f:
#     for line in f:
#         tokens = prepare_text_for_lda(line)
#         if random.random() > .99:
#             print(tokens)
#             text_data.append(tokens)
#             
# =============================================================================
for line in txtfile:
    tokens = prepare_text_for_lda(line)
    if tokens != [] : 
        #print(tokens)
        text_data.append(tokens)
            


#Forming dictionary & Corpus
def getCorpDict():
    from gensim import corpora
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]
    
    #saving corpus & dictionary for later use
    import pickle
    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')
    
    return corpus,dictionary


