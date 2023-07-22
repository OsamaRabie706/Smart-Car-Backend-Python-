from django.db import models


class client(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=256)
    car_model = models.CharField(max_length=256)
    car_id = models.CharField(max_length=256)