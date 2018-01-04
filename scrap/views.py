from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import StockSerializer
from .script.scrap import CoinMarkeCap
from .script.create_database import create_db
from .models import Post
import ast
import datetime
from dateutil import parser
import json
import pandas as pd
import time


class StockList(APIView):

    def get(self, request):
        stock = Post.objects.all()
        serilizer = StockSerializer(stock, many=True)
        return Response(serilizer.data)

    def post(self):
        pass




#/table/
def table(request):
    x = CoinMarkeCap().run()
    cols = ['Rank', 'Name', 'Symbol', 'Graph(7d)', 'Price_usd', '24h_volume_usd', 'Market_cap_usd',  'Max_supply',  'Percent_change_24h', 'Last_updated']
    return render(request, 'table.html', {"content":{"headings":cols,
                                                    "results":x
                                                    }})
#/<rank>/
def chart(request, rank=None):            
    return render(request, "chart_page.html", {"rank":rank})


def json_page(request, rank=None):
    post = eval(Post.objects.filter(rank=rank)[0].history)
    data = []
    for dt in post:
        utc_time = time.mktime(pd.to_datetime(dt["Date"]).timetuple())
        data.append([round(utc_time)*1000,ast.literal_eval(dt["Open"])])
    data =   list([data[-90:]])
    
    return HttpResponse( data, content_type="text/json")

def datatable(request):
    return render(request, "datatable.html")
    
def home(request):
    x = CoinMarkeCap().run()
    try:
        create_db
    except:
        pass
    cols = ['Rank', 'Name', 'Symbol', 'Graph(7d)', 'Price_usd', '24h_volume_usd', 'Market_cap_usd',  'Max_supply',  'Percent_change_24h', 'Last_updated']
    return render(request, 'home.html', {"content":{"headings":cols,
                                                    "results":x
                                                    }})
