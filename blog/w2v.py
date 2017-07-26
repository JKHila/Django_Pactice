import gensim
import json

a = gensim.models.word2vec.Word2Vec.load("blog/tourplanb_place_saved_word2vec_model")

def getWordsJson(word):
    try:
        jsonStr = json.dumps(a.most_similar(positive=word, negative=""))      
        return json.loads(jsonStr) 
        pass
    except Exception as e:
        return e

def getWords(word):
    try:
        names = [key[0] for key in a.most_similar(positive=word, negative="")]
        return names 
        pass
    except Exception as e:
        return e
