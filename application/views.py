from cgitb import lookup
from cmath import pi
from multiprocessing import context
from django.shortcuts import render,HttpResponse
import requests
from .models import Covidcases
import datetime
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.
from .serializers import CovidSerializer
from rest_framework.response import Response


def dashboard(request):
    if request.GET:
        context={}
        date=request.GET.get('getdate')
        cases=Covidcases.objects.filter(date=date).values('country','total_case')
        casesdict={}
        # print(cases)

        for i in cases:
            # print(i)

            casesdict[i['country']]=i['total_case']

        countrylist=list(casesdict.keys())
        totalcaselist=list(casesdict.values())

        context['countrylist']=countrylist
        context['totalcaselist']=totalcaselist
        # context['base']="USD"
        context['date']=str(date)
        # print(context['date'])
        print(countrylist,totalcaselist)
        return render(request,'application/dashboard.html',context)

    context={}
    today_date=datetime.datetime.today().date()
    cases=Covidcases.objects.filter(date=today_date).values('country','total_case')
    casesdict={}
    # print(cases)

    for i in cases:
        # print(i)

        casesdict[i['country']]=i['total_case']

    countrylist=list(casesdict.keys())
    totalcaselist=list(casesdict.values())

    context['countrylist']=countrylist
    context['totalcaselist']=totalcaselist
    # context['base']="USD"
    context['date']=str(today_date)
    # print(context['date'])
    # print(countrylist,totalcaselist)
    return render(request,'application/dashboard.html',context)


def get_data(request):

    try: 
        url = "https://covid-193.p.rapidapi.com/statistics"

        headers = {
            "X-RapidAPI-Key": "eba8bf64c0msha8d7872eae06eccp147836jsn25ca06e40347",
            "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)

        # print(response.json())

        for i in range(0,20):
            country=response.json()['response'][i]['country']
            total_case=response.json()['response'][i]['cases']['total']
            date=response.json()['response'][i]['day']
            c=Covidcases(country=country,total_case=total_case,date=date)
            c.save()
        return HttpResponse("Data successfully added !")            

    except:
        # print('can not run get data in application view')
        return HttpResponse("Data not added !")


class CR_CovidApiView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Covidcases.objects.all()
    serializer_class=CovidSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def  post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

        
        
        

class U_CovidApiView(GenericAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
    queryset=Covidcases.objects.all()
    serializer_class=CovidSerializer
    lookup_field="id"

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

class Getbydate_ExchangeApiView(GenericAPIView):
    queryset=Covidcases.objects.all()
    serializer_class=CovidSerializer
    def get(self,request,date=None):
        queryset            =   Covidcases.objects.filter(date=date)
        # print(queryset)
        serialize           =   CovidSerializer(queryset,many=True,context={'request': request})
        # print(serialize.data)
        return Response(serialize.data)

class Getbycountry(GenericAPIView):
    queryset=Covidcases.objects.all()
    serializer_class=CovidSerializer
    def get(self,request,country=None):
        queryset            =   Covidcases.objects.filter(country=country)
        # print(queryset)
        serialize           =   CovidSerializer(queryset,many=True,context={'request': request})
        # print(serialize.data)
        return Response(serialize.data)

# class Getbydaterange_ExchangeApiView(GenericAPIView):
#     queryset=Exchange.objects.all()
#     serializer_class=ExchangeSerializer
#     def get(self,request,fromdate=None,todate=None):
#         # fromdate=self.request.GET.get('fromdate')
#         # todate=self.request.GET.get('todate')
#         print(fromdate,todate)
#         queryset            =   Exchange.objects.filter(response_date__gte=fromdate,response_date__lte=todate)
#         serialize           =   ExchangeSerializer(queryset,many=True,context={'request': request})
#         return Response(serialize.data)


# import time
# import datetime
# Initiating = True
# print(datetime.datetime.now())
# while True:
#     if Initiating == True:
#         print("Initiate")
#         print( datetime.datetime.now())
#         time.sleep(60 - time.time() % 60+5)
#         Initiating = False
#     else:
#         time.sleep(60)
#         print("working")
#         print(datetime.datetime.now())

