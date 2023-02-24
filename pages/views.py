from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.http import HttpResponse, JsonResponse

person = {}


def homePageView(request):
    return HttpResponse("Hello, World!")


def firstRoute(request):
    # person = {
    #     'first_name': 'Jeff'
    # }
    return JsonResponse(person)


def post(request):
    person = request.validated_data
    person = {
        'first_name': 'Jeff'
    }
    return JsonResponse(person)
