from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import JsonResponse

from .w2v import *

def var_json(request):
    place = ""
    lang = ""
    cate = ""
    req = request.GET
    if request.method == 'GET' and 'name' in req:
        place += (req["name"])
    if request.method == 'GET' and 'lang' in req:
        lang = req["lang"]
    if request.method == 'GET' and 'cate' in req:
        cate = req["cate"]
        place += ",c"+req["cate"]
    
    if not place or not cate or not lang:
        places = json.loads(json.dumps(makeJson([],200,"have no parameter")))
    else:
        places = getWordsJson(place,lang,cate)
    return JsonResponse(places, safe=False)
