from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome!")
    # return render(request, 'textutilizer.html')

def removepunctuations(request):
    input_text = request.POST.get('text', 'default')  
    removepunctuations_checked = request.POST.get('removepunctuations', False)  
    removespaces_checked = request.POST.get('removespaces', False)
    capitalize_checked = request.POST.get('capitalize', False)

    punctuations = '''}{!@£$%^&*()_+-="'\][/.,`~]'''
    analyzed_text = ''
    context = {'task': '', 'analyzed_text': analyzed_text}

    if removepunctuations_checked: 
        for char in input_text:
            if char not in punctuations:
                analyzed_text += char
        context['task'] = 'Removed Punctuations!'
        context['analyzed_text'] = analyzed_text
    elif removespaces_checked:
        context['task'] = 'Removed Spaces!'
        analyzed_text = input_text.replace(' ', '')
        context['analyzed_text'] = analyzed_text
    elif capitalize_checked:
        context['task'] = 'Capitialized the text!'
        analyzed_text = input_text.upper()
        context['analyzed_text'] = analyzed_text
    else:
        return HttpResponse('You have to select an option in order to analyze your text!')


    

    return render(request, 'analyzed.html', context)
