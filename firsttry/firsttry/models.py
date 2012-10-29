from django.db import models


class Counter(models.Model):
	number = models.IntegerField()
	