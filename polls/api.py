from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .models import Votes
from django.http import JsonResponse
import json


@csrf_protect
def search(request):
    name = request.POST['name_field']
    name_search = Votes.objects.filter(first_name__contains=name).values()
    cont = {'test': list(name_search)}
    return JsonResponse(cont, status=200)
