from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from ratelimit.decorators import ratelimit

# Create your views here.
rate =1000

@ratelimit(key='ip', rate=f'{rate}/m', block = True, method = ratelimit.ALL)
def simpleview(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        return JsonResponse("You've used the wrong method.", safe= False, status = status.HTTP_405_METHOD_NOT_ALLOWED)