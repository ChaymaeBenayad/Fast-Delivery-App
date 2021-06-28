from django.db import models

# Create your models here.
class Repere(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)
	description = models.TextField(null=False, blank=False)
	photo = models.ImageField(upload_to='images',blank=False)

	
	def  __str__(self):
		return self.name
