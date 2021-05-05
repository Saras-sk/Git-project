from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def Analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # check which checbox is on
    if removepunc == "on":
        # analyzed = djtext
        punctuations = ''',.';/[]\=-)()[]{}|~!@#$%^&*""'''''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'Analyzed_text': analyzed}
        djtext = analyzed
#         return render(request, 'Analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to upper case', 'Analyzed_text': analyzed}
        djtext = analyzed
#         return render(request, 'Analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'Analyzed_text': analyzed}
        djtext = analyzed
#         return render(request, 'Analyze.html', params)
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extraspaceremover', 'Analyzed_text': analyzed}
        djtext = analyzed
     return render(request, 'Analyze.html', params)
    


