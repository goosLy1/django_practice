# from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Person
def index(request):
    people = Person.objects.all()
    people_json = serializers.serialize('json', people)
    return JsonResponse(people_json, safe=False)