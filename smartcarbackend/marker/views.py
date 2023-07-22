import struct

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import time

import snap7
"""db_number=1
start_offset=256
bit_offset=0
value = 0"""
plc_ip="192.168.0.2"

finished = False



def read_marker(start_add,length):
    client = snap7.client.Client()
    client.connect(plc_ip, 0, 1)
    data = client.read_area(snap7.types.Areas.MK,0,start_add,length)
    if data==bytearray(b'\x00')*length:
        return False
    else:
        print(data) #to be explained....
        return True



def readMemoryArea(start_address,length):
    client = snap7.client.Client()
    client.connect(plc_ip, 0, 1)
    reading = client.read_area(snap7.types.Areas.MK, 0, start_address, length)
    value = struct.unpack('>f', reading)  # big-endian
    return value

def index(request):
    return HttpResponse('Hello')

def client_data(request):
    return HttpResponse('client data')

def time_remain(request):
    data = [
        {
            'id':1,
            'value':int(readMemoryArea(1020,4)[0])
        }
    ]
    return JsonResponse(data, safe=False)

def alarm_marker(request):
    data = [
        {
            'id': 1,
            'value': read_marker(0,7)
        }
    ]
    return JsonResponse(data, safe=False)

def data(request):
    data = [
        {
            'id': 1,
            'value' : read_marker(0,7)
        },{
            'id': 2,
            'value' : read_marker(7,7)
        },{
            'id': 3,
            'value' : read_marker(14,7)
        },{
            'id': 4,
            'value' : read_marker(21,7)
        },{
            'id': 5,
            'value' : read_marker(42,7)
        },{
            'id': 6,
            'value' : read_marker(200,7)
        },{
            'id': 7,
            'value' : read_marker(207,7)
        },
    ]
    return JsonResponse(data, safe=False)
# Create your views here.
