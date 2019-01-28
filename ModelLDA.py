# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 12:15:48 2018

@author: jdhruwa
"""
def LDA(jd,cv):
    import gensim
    from makeDictionary import getCorpDict
    corpdict=getCorpDict(jd)

    corpora=corpdict[0]
    dictionary=corpdict[1]
    # =============================================================================
    # dictionary.filter_tokens(bad_ids=[dictionary.token2id['etc']])
    # dictionary.compactify()
    # =============================================================================

    NUM_TOPICS = 10
    ldamodel = gensim.models.ldamodel.LdaModel(corpora, num_topics = NUM_TOPICS, id2word=dictionary, passes=43)
    #ldamodel.save('model10.gensim')
    topics = ldamodel.print_topics(num_words=4)
    for topic in topics:
       print(topic)

    #Document testing 
    from tokenizer import prepare_text_for_lda
    from fileRead import get_text
    new_doc=get_text(cv)
    #new_doc=get_text("../CV/86357_FS_Jinendra_Khot.docx")
    new_doc = prepare_text_for_lda(new_doc)
    new_doc_bow = dictionary.doc2bow(new_doc)
    #print(new_doc_bow,"\n\n")

    from operator import itemgetter
    selectedTopic=ldamodel.get_document_topics(new_doc_bow)
    selectedTopic.sort(key=itemgetter(1,0),reverse=True)
    #print("Selected Topics (Sorted a/c to relevance):\n",selectedTopic)

    #Calculate approximate match percentage
    match_perc=[ele[1]*100 for ele in selectedTopic if ele[1]>0.1]
    match_perc.extend([ele[1]*10 for ele in selectedTopic if ele[1]<0.1])
    match_perc=sum(match_perc)
    return match_perc

#print("Match Percentage: ",match_perc)
#take pickled data & show results
#corpus =corpora
#lda = gensim.models.ldamodel.LdaModel.load('model10.gensim')
#import pyLDAvis.gensim
#lda_display = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort_topics=False)
#pyLDAvis.display(lda_display)

#open result in  browser
#pyLDAvis.show(lda_display)

# =============================================================================
# pyLDAvis.save_html(lda_display,"pylda.html")
# =============================================================================
