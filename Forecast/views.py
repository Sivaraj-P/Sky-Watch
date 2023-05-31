from django.shortcuts import render,redirect
from datetime import date
import datetime as dt
import requests
import math


def check_location(CITY):
    
    API_KEY="" #add you api key from open weather
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}"
    
    return( requests.get(url).json())


def report(request):
    if request.method=='POST':
        location=request.POST["location"].lower()
        response=check_location(location)
        try:
            context = {
                
                "city_name":response["city"]["name"],
                "city_country":response["city"]["country"],
                "sunrise":(str(dt.datetime.utcfromtimestamp(response["city"]["sunrise"]+response["city"]["timezone"])))[11:16],
                "sunset":(str(dt.datetime.utcfromtimestamp(response["city"]["sunset"]+response["city"]["timezone"])))[11:16],
                "wind":(response['list'][0]['wind']['speed']),
                "degree":response['list'][0]['wind']['deg'],
                "status":response['list'][0]['weather'][0]['description'],
                "cloud":response['list'][0]['clouds']['all'],
                'date':response['list'][0]["dt_txt"],
                'date1':(response['list'][1]["dt_txt"])[8:10],
                'time1':(response['list'][1]["dt_txt"])[11:16],
                'date2':response['list'][2]["dt_txt"][8:10],
                'time2':response['list'][2]["dt_txt"][11:16],
                'date3':response['list'][3]["dt_txt"][8:10],
                'time3':response['list'][3]["dt_txt"][11:16],
                'date4':response['list'][4]["dt_txt"][8:10],
                'time4':response['list'][4]["dt_txt"][11:16],
                'date5':response['list'][5]["dt_txt"][8:10],
                'time5':response['list'][5]["dt_txt"][11:16],
                'date6':response['list'][6]["dt_txt"][8:10],
                'time6':response['list'][6]["dt_txt"][11:16],


                "temp": round(response["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(response["list"][1]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(response["list"][1]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(response["list"][2]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(response["list"][2]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(response["list"][3]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(response["list"][3]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(response["list"][4]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(response["list"][4]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(response["list"][5]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(response["list"][5]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(response["list"][6]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(response["list"][6]["main"]["temp_max"] -273.0),


                "pressure":response["list"][0]["main"]["pressure"],
                "humidity":response["list"][0]["main"]["humidity"],
                "sea_level":response["list"][0]["main"]["sea_level"],


                "weather":response["list"][1]["weather"][0]["main"],
                "description":response["list"][1]["weather"][0]["description"],
                "icon":response["list"][0]["weather"][0]["icon"],
                
            }
            return render(request, "report.html", context=context)
        except:

            return render(request, "failed.html")
    else:
        today=date.today()
        current_date= today.strftime("%d %B %Y")
        
        context={
        'present_date':current_date,
        }
        return render(request,'home.html',context=context)




    