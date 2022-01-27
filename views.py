from http.client import HTTP_PORT
from string import punctuation
from tkinter import OFF, ON
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render  (request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'off')
    capital = request.GET.get('capital', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    newlinerem = request.GET.get('newlineremover', 'off')
    charcount = request.GET.get('charcount', 'off')

    if removepunc == "on": 
        analyzed = djtext
        punctuation = '''!()[]{};.:/,'"\?@#$%^&*_~<>'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Puncations', 'analyzed_text': analyzed}
        #Analyze the text 
        return render(request, 'analyz.html', params)
    elif capital == "on":
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
        params = {'purpose': 'UPPER CASE', 'analyzed_text': analyze}
        return render(request, 'analyz.html', params)
    elif newlinerem == "on":
        analyze = ""
        for char in djtext:
            if char != "\n":
                analyze = analyze + char

        params = {'purpose': 'line remover', 'analyzed_text': analyze}
        return render(request, 'analyz.html', params)
    elif spaceremover == "on":
        analyze = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]== " "):
                analyze = analyze + char
           
        params = {'purpose': 'line remover', 'analyzed_text': analyze}
        return render(request, 'analyz.html', params)
    elif charcount == "on":
        analyze = len(djtext)
        params = {'purpose': 'charcater count', 'analyzed_text': analyze}
        return render(request, 'analyz.html', params)
    else:
        return HttpResponse("error")

#def capfirst(request):
    #return HttpResponse("capitalize first")

#def newlineremover(requset):
    return HttpResponse("new line remover")

#def spaceremove(request):
    return HttpResponse("space remover    <a href='/'>back </a>")

#def charcount(request):
    return HttpResponse("char count")
