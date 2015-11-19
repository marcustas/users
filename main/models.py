from django.db import models
from django.contrib.auth.models import User
import datetime
import random

# Create your models here.
def random100():
	return random.randint(1, 100)

class CustomUser(models.Model):
	user = models.OneToOneField(User)
	bdate = models.DateField('Birth date', null=True, blank=True)
	random = models.IntegerField(default=random100)
