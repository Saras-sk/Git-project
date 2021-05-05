from django.http import HttpResponse
from django.shortcuts import render


#
# def index(request):
#     return HttpResponse('''<h1>PERSONEL NAVIGATOR</h1> <h1>Saras</h1> <a href="https://www.facebook.com/saras.singh.104"> This is my facebook profile</a>>''')
#
#
# def about(request):
#     return HttpResponse("about SARAS")
def index(request):
    return render(request, 'index.html')


def Analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    # check checkbox value
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    # check which checbox is on
    if removepunc == "on":
        # analyzed = djtext
        punctuations = ''',.';/[]\=-)()[]{}|~!@#$%^&*""'''''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'Analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)
    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to upper case', 'Analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)
    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'Analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)
    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'extraspaceremover', 'Analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)
    else:
        return HttpResponse("Error")

# def capitalizefirst(request):
#     return HttpResponse("capitalize first")
#
#
# def newlineremove(request):
#     return HttpResponse("newline remover")
