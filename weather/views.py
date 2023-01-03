from django.shortcuts import render, redirect
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

from rest_framework.views import APIView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


  
# def index(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         print('name',city)
#         # source contain JSON data from API
  
#         source = urllib.request.urlopen('http://api.waqi.info/feed/dhaka/?token=a5218cca1fa68b181689e9d32795a1c987730f53').read()
#         # converting JSON data to a dictionary
#         list_of_data = json.loads(source)
  
#         # data for variable list_of_data
#         data = {
#             "country_code": str(list_of_data['data']['forecast']['daily']['pm10'][0]['avg']),
#         }
#         # print(list_of_data)
#     else:
#         data ={}
#     return render(request, "weather/index.html",{'data':data})


# def postdata(request):
#     if request.method == 'POST':
#         city = request.POST.get('city')
#         print('name',city)
#         # source contain JSON data from API
  
#         source = urllib.request.urlopen('http://api.waqi.info/feed/dhaka/?token=a5218cca1fa68b181689e9d32795a1c987730f53').read()
#         # converting JSON data to a dictionary
#         list_of_data = json.loads(source)
  
#         # data for variable list_of_data
#         data = {
#             "country_code": str(list_of_data['data']['forecast']['daily']['pm10'][0]['avg']),
#         }
#         # print(list_of_data)
#     else:
#         data ={}


@method_decorator(csrf_exempt, name = 'dispatch')
class CityApi(APIView):

    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        city = data.get("city")
        print(city)
        source = urllib.request.urlopen('http://api.waqi.info/feed/'+city+'/?token=a5218cca1fa68b181689e9d32795a1c987730f53').read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['data']['forecast']['daily']['pm10'][0]['avg'])
        }
        sum = (list_of_data['data']['forecast']['daily']['pm10'][0]['avg'])+(list_of_data['data']['forecast']['daily']['pm10'][1]['avg'])+(list_of_data['data']['forecast']['daily']['pm10'][2]['avg'])
        avg = sum/3
        print(avg)
        dict = {"city" : city, "avg": avg}

        return JsonResponse(dict)



#Working with form data
from .forms import CityForm
from .models import City
def addcity(request):
    if request.method == "POST":
        fm = CityForm(request.POST)

        if fm.is_valid():
            
            city = fm.cleaned_data['city']
            print('name',city)
            
            source = urllib.request.urlopen('http://api.waqi.info/feed/'+city+'/?token=a5218cca1fa68b181689e9d32795a1c987730f53').read()
        # converting JSON data to a dictionary
            list_of_data = json.loads(source)
  
        # data for variable list_of_data
            data = {
            "country_code": str(list_of_data['data']['forecast']['daily']['pm10'][0]['avg'])
        }
            sum = (list_of_data['data']['forecast']['daily']['pm10'][0]['avg'])+(list_of_data['data']['forecast']['daily']['pm10'][1]['avg'])+(list_of_data['data']['forecast']['daily']['pm10'][2]['avg'])
            avg = sum/3
            print(avg)
            reg = City(city=city)
            reg.save()
            fm = CityForm()
            return render(request, 'weather/index.html', {
        'data':avg
    })
    else:
        fm = CityForm()
    stud = City.objects.all()
    
        # print(list_of_data)
    return render(request, 'weather/index.html', {
        
    })
