import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import time

from clients.models import client


def read_data(request):
    response = request.body
    print(response)
    return HttpResponse("client data")

def write_data(request):
    response = request.body
    user_name = json.loads(response)["userName"]
    phone_number = json.loads(response)["phoneNmuber"]
    car_model = json.loads(response)["carModel"]
    car_id = json.loads(response)["carId"]
    obj = client()
    obj.user_name = user_name
    obj.phone_number = phone_number
    obj.car_model = car_model
    obj.car_id = car_id
    obj.save()
    data = [
        {
            'id': obj.id,
            'userName': obj.user_name,
            'phoneNmuber': obj.phone_number,
            'carModel': obj.car_model,
            'carId': obj.car_id
        }]
    print(data)
    return JsonResponse(data,safe=False)

def get_data_by_id(request):
    clientx = client.objects.all().filter(id=72).values()[0]

    data = [
        {
            'id': clientx.get("id"),
            'userName': clientx.get("user_name"),
            'phoneNmuber': clientx.get("phone_number"),
            'carModel': clientx.get("car_model"),
            'carId': clientx.get("car_id")
        }]
    print(data)
    return HttpResponse(data)