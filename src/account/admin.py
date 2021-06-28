from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


class AccountAdmin(UserAdmin):
	list_display = ('identifiant', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin')
	search_fields = ('identifiant','last_name')
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	
	ordering = ('identifiant',)


admin.site.register(Account, AccountAdmin)