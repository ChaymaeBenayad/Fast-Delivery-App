from django.contrib import admin
from landmark.models import Repere

# Register your models here.
class RepereTab():
	list_display = ('name','description')
	search_fields = ('name')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Repere)