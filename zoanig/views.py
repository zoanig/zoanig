from django.http import HttpResponse
from django.shortcuts import render

def profile(request):
    accept_header = request.META.get('HTTP_ACCEPT', '')
    condition = 'text/html' in accept_header
    filename = f'profile{".base" if condition else ''}.txt' 
    with open(filename, 'r') as file:
        content = file.read()
        return HttpResponse(content, content_type="text/plain") if not condition else render(request, 'index.html', {'content':content})
