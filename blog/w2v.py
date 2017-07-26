import gensim
import json
from .dbConn import *


def compareCate(cate,names):
    nameStr = ""
    for key in names:
        nameStr += "\'"+key+"\',"
    nameStr = nameStr[0:len(nameStr)-1]

    query = "SELECT Title"
    query +="   FROM place_info "
    query += "  WHERE Category="+cate
    query += "  AND Title IN ("+nameStr+")"

    print (query)
    dbResult = getQuery(_query=query)
    return dbResult

def getWordsJson(word,ln,cate):
    if ln == "zh":
        a = gensim.models.word2vec.Word2Vec.load("blog/tourplanb_place_saved_word2vec_model")
    elif ln == "en":
        a = gensim.models.word2vec.Word2Vec.load("blog/tourplanb_place_saved_word2vec_model")
    else:
        a = gensim.models.word2vec.Word2Vec.load("blog/tourplanb_place_saved_word2vec_model")            
    try:
        words = word.split(",")
        b = a.most_similar(positive=words, negative="", topn=20)
        names = [key[0] for key in b]
    
        jsonStr = json.dumps(compareCate(cate,names))      
        return json.loads(jsonStr) 
        pass
    except Exception as e:
        return e













def getWords(word):
    try:
        return names 
        pass
    except Exception as e:
        return e
