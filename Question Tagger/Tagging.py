# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Last Updated Date:7/8/2015

import re
from gensim.models import word2vec


class Tagging():
    __StopWords=["a", "able", "about", "across", "after", "all", "almost", "also", "am",

                "among", "an","and","any","are","as","at","be","because","been","but","by","can",

                "cannot","could","dear","did","do","does","either","else","ever","every",
                
                "for","from","get","got","had","has","have","he","her","hers","him","his",
                
                "how","however","i","if","in","into","is","it","its","just","least","let",
                
                "like","likely","may","me","might","most","must","my","neither","no","nor",
                
                "not","of","off","often","on","only","or","other","our","own","rather","said",
                
                "say","says","she","should","since","so","some","than","that","the","their",
                
                "them","then","there","these","they","this","tis","to","too","twas","us",
                
                "wants","was","we","were","what","when","where","which","while","who",
                
                "whom","why","will","with","would","yet","you","your","?"]
    
    __model=word2vec.Word2Vec.load_word2vec_format("C:/Users/Adithya/Desktop/GoogleNews-vectors-negative300.bin.gz",binary=True)
    __model.init_sims(replace=True)
    __threshold=0.6
    __numberOfTags=5
    #Passed input.Punctuations removes and question split. 
    def __init__(self,question):
        self.question=re.sub("[^a-zA-Z]"," ",question).split()
        
    #Stop words are removed
    def __removeStopWords(self):
        self.question=[word for word in self.question if word not in Tagging.__StopWords]
    
	#Finding similar words for each word of the question    
    def __findSimilarity(self):
        self.__similarity=[];
        [[self.__similarity.append(similar) for similar in Tagging.__model.most_similar(word,topn=Tagging.__numberOfTags)]for word in self.question]
            
    #sorting and returning top N tags
    def __topTags(self):
        self.tags=[];
        for i in range(0,Tagging.__numberOfTags):
            self.tags.append(sorted(self.__similarity,key=lambda x: x[1],reverse=True)[i][0])
            
    #calling all the methods required to return top N Tags
    def findTags(self):
        self.__removeStopWords()
        self.__findSimilarity()
        self.__topTags()
        return (self.tags)
        
        
