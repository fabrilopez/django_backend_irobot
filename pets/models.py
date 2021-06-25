from django.db import models

class Pet(models.Model):
	name = models.CharField(max_length=50, blank=False, default='')
	age = models.PositiveIntegerField(blank=False, default=0)
	exact_age = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	