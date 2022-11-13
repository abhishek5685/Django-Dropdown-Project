from django.shortcuts import render
from world.models import *
from django.http import JsonResponse , HttpResponse
import json

# Create your views here.

def home(request):
    if request.method == "GET":
        context = {}
        country_list=Country.objects.all()
        state_list = State.objects.all()
        city_list = City.objects.all()
        context['country_list'] = country_list
        context['state_list'] = state_list
        context['city_list'] = city_list      
    return render(request, "home.html", context)

def state_data(request):
    if request.method == "GET":
        context = {}
        country_by = request.GET.get("country_id")
        country_by_id = int(country_by)
        print(type(country_by_id))
        state_list = State.objects.filter(country_id= country_by_id)
        print("+++++++++++++++++_____________+++++++++++")
        print(state_list)
        return JsonResponse(list(state_list.values("id", "name")), safe=False)

