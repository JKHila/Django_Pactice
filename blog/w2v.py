import gensim
import json
from .dbConn import *

def getTable(names,similar):
    nameStr =""
    rank = 0
    
    for i in range(len(names)):
        nameStr += "    select \'"+names[i]+"\',\'"+str(rank)+"\' , \'"+str(similar[i])+"\' union "
        rank += 1
    return nameStr[0:len(nameStr)-6]
    

def filterData(cate,names,similar,lang):
    
    table = getTable(names,similar)
    if lang=="zh":
        lang="zh-CN"

    query = "SELECT Title,idx,similar"
    query +="   FROM place_info p"
    query +="   JOIN( SELECT * FROM"
    query +="           (select null as \'name\',null as \'rank\',null as \'similar\' union"
    query +=    table
    query +="       )as b"
    query +="   )as c"
    query += "  WHERE p.Category="+cate
    query += "  AND p.Title = c.name"
    query += "  AND p.LanguageCode = \'"+lang+"\'"
    query += "  ORDER BY c.rank"

    #print (query)
    dbResult = getQuery(_query=query)
    return dbResult

def makeJson(arr,status,message):
    json = dict()
    json['status'] = status    
    json['message'] = message
    
    placeList = {}
    placeArr = []

    for key in arr:
        place = dict()
        place['idx'] = key[1]
        place['similarity'] = key[2]
        place['placeName'] = key[0]
        placeArr.append(place)

    placeList['placeList'] = placeArr

    json['data'] = placeList
    json['mode'] = "Recomendation"
    json['copyright'] = "© 2017 Dabeeo, Inc"
    
    return json


def getWordsJson(word,lang,cate):
    a = gensim.models.word2vec.Word2Vec.load("blog/tourplanb_place_saved_word2vec_model")
    try:
        words = word.split(",")
        b = a.most_similar(positive=words, negative="", topn=20)
        names = [key[0] for key in b]
        similar = [key[1] for key in b]
    
        fDate = filterData(cate,names,similar,lang)
        
        if not fDate:
            raise Exception
        else:
            jsonStr = json.dumps(makeJson(fDate,200,"ok"))

        pass
    except Exception as e:
        jsonStr = json.dumps(makeJson([],200,"have no data"))
    finally:
        return json.loads(jsonStr)
        











