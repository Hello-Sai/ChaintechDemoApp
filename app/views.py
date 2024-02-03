from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib import messages
import requests
from app.models import Person

# Create your views here.
def index(request):
    if request.method=="GET":
        data,ip = get_weather_information()
        return render(request,'index.html',{'time':get_current_time(),'weather':data,'ip':ip})
    

def register(request):
    try:
        if request.method=="POST":
            person = Person.objects.create(username= request.POST["username"],
            email = request.POST["email"],
            phone_number = request.POST['phone_number'],
            address = request.POST['address'])
            messages.success(request,"Successfully Registered details")
            return redirect('/')
    except Exception as e:
        messages.error(request,e,'danger')
    return render(request,'register.html')
def get_current_time():
    return datetime.now()

def get_weather_information():
    data,ip = get_latitude_longitude()
    API_KEY ='e98617d09a1b7b2f634ff99c02ef61dd'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={data.get("latitude")}&lon={data.get("longitude")}&date={str(datetime.today()).split()[0]}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    data =  data.get('main')
    if data:
        return int(data.get('temp')-273.15),ip
    else:
        return None,ip
def get_latitude_longitude():
    try:
        ip = get_current_ip()

        url = "https://community-neutrino-ip-info.p.rapidapi.com/ip-info"

        payload = {
            "ip": str(ip),
            "reverse-lookup": "checked"
        }
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "eea54fdd3bmsh446d5b0d38bf9d9p12bdf7jsn36b2971b04fa",
            "X-RapidAPI-Host": "community-neutrino-ip-info.p.rapidapi.com"
        }

        response = requests.post(url, data=payload, headers=headers)

        return response.json(),ip
    except Exception as e:
        return e
def get_current_ip():
    url = "https://httpbin.org/ip"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('origin')
    return None
def records(request):
    persons = Person.objects.all()
    return render(request,'records.html',locals())