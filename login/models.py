from random import randint
from django.db import models


class UserInfo(models.Model):
    phone_number = models.CharField(max_length=11)


class KavanegarOTP(models.Model):
    API_KEY = 'your_api_key'
    token = randint(1000, 9999) 



