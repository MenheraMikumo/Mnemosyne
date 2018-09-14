from django.shortcuts import render

# Create your views here.

def index(requests):

    context_dict = {}
    response = render(requests, 'report.html', context=context_dict)

    return response
