import gensim
import json

a = gensim.models.word2vec.Word2Vec.load("blog/tourplanb_place_saved_word2vec_model")

def getWords(word):
    try:
        return json.dumps(a.most_similar(positive=word, negative=""))
        pass
    except Exception as e:
        return e
