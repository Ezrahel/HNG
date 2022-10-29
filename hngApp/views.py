from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(["GET"])
def home(request, *args, **kwargs):
  header = {"Access-Control-Allow-Origin":"*"}
  data = {
    "slackUsername":"Ez'rahel",
    "backend":True,
    "age": 24,
    "bio":"Am a backend engineer, am comfortable with python django"
  }
  return JsonResponse(data,headers=header)