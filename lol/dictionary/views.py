from django.shortcuts import render,redirect
import json
from difflib import get_close_matches
import os

data = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'data.json')))

# Create your views here.

def word(request, string):
    string = string.lower()
    shits = data[string]
    return render(request,'word.html',{'shits':shits})

def confirm(request, string):
    if request.method == 'POST':
        ans = request.POST.get('ans')
        if(ans.lower()=='y'):
            return redirect(word, string = string)
        else:
            return render(request,'error.html')
    else:
        return render(request, 'confirm.html', {'string' : string})

def home(request):
    if request.method == 'POST':
        inp = request.POST.get('word')
        print(type(inp))
        inp = inp.lower()
        if inp in data.keys():
            return redirect(word, string = inp)
        elif len(get_close_matches(inp, data.keys())) > 0:
            return redirect(confirm, string = get_close_matches(inp, data.keys())[0])
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'index.html')
