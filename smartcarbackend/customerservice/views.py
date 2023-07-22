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




def writeMemory(start_address,length,data):
    client = snap7.client.Client()
    client.connect(plc_ip, 0, 1)
    client.mb_write(start_address, length, data)  # big-endian


def start(request):
    writeMemory(500, 7, bytearray(b'\x80\x00\x00\x00\x00\x00\x00'))
    writeMemory(500, 7, bytearray(b'\x00\x00\x00\x00\x00\x00\x00'))
    data = [
        {
            'value': True
        }
    ]
    return JsonResponse(data, safe=False)


def stop(request):
    writeMemory(600, 7, bytearray(b'\x80\x00\x00\x00\x00\x00\x00'))
    writeMemory(600, 7, bytearray(b'\x00\x00\x00\x00\x00\x00\x00'))
    data = [
        {
            'value': True
        }
    ]
    return JsonResponse(data, safe=False)