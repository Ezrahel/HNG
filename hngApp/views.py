from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def api_response(request, *args, **kwargs):
    return JsonResponse({"slackUsername":"Ezrahel","Backend": True,"Age":24,"Bio":"Am a backend engineer, am comfortable with python,django HTML&CSS. Fun fact: Am a Tech enthusiast and a table tennis geek"})