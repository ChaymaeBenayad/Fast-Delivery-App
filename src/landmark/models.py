from django.db import models

# Create your models here.
class Repere(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	photo = models.ImageField(upload_to='images',blank=True)

	
	def  __str__(self):
		return self.name
