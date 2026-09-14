from django.http import HttpResponse
from django.shortcuts import render
from profile_generater import generate_fetch_layout, DATA, ASCII_ART
import requests
def profile(request):
    accept_header = request.META.get('HTTP_ACCEPT', '')
    condition = 'text/html' in accept_header
    return HttpResponse(generate_fetch_layout(DATA, ASCII_ART), content_type="text/plain") if not condition else render(request, 'index.html', {'DATA': DATA, 'ASCII': ASCII_ART})

def theme(request):
    accept_header = request.META.get('HTTP_ACCEPT', '')
    condition = 'text/html' in accept_header
    if not condition:
        with open('theme.txt', 'r') as file:
            output = file.read()
    else:
        output = 'This endpoint only supports a terminal'
    return HttpResponse(output, content_type="text/plain")
