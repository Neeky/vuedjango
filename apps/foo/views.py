from django.shortcuts import render
from django.utils.timezone import now
from django.http.response import JsonResponse
# Create your views here.

def current_time(request):
    """
    """
    return JsonResponse(
        {'ct': now()}
    )
    

