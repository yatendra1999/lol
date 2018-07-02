from django.shortcuts import render
import json
from difflib import get_close_matches
import os

def translate(w, data):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = get_close_matches(w, data.keys())[0]
        return data[yn]
    else:
        return "The word doesn't exist. Please double check it."


# Create your views here.

def word(request, string):
    BS_DIR = os.path.dirname(os.path.abspath(__file__))
    data = json.load(open(os.path.join(BS_DIR,'data.json')))
    shits = translate(string, data)
    print(shits)
    return render(request,'word.html',{'lol':shits})
