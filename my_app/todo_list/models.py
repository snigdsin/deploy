from django.db import models

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	def __str__(self):
   		return self.item + ' | ' + str(self.completed)

class revenue(models.Model):
	Region = models.CharField(max_length=50)
	Profit = models.FloatField()

	def __str__(self):
		return self.Region


