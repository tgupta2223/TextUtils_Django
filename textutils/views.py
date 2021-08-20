from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About - Hello World!")

def analyze(request):
    # get the text
    djtext = request.POST.get("text", "default")
    
    # Get checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # check if checkbox is on
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        djtext = analyzed
        params = {'purpose':'Changed to uppercase', 'analyzed_text': analyzed}

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed += char
        djtext = analyzed
        params = {'purpose':'Removed NewLines', 'analyzed_text': analyzed}

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        djtext = analyzed
        params = {'purpose':'Removed Extra Spaces', 'analyzed_text': analyzed}
 
    if (charcount == "on"):
        analyzed = len(djtext)         
        params = {'purpose':'Total Characters Count', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("Please select any of the operation.")

    return render(request, 'analyze.html', params)