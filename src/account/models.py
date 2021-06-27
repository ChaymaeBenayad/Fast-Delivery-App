from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self, identifiant, password=None):
		if not identifiant:
			raise ValueError('un utilisateur doit avoir un identifiant!')

		user = self.model(
			identifiant=identifiant,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, identifiant, password):
		user = self.create_user(
			identifiant=identifiant,
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	identifiant             = models.CharField(verbose_name="identifiant", max_length=5, unique=True)
	first_name              = models.CharField(max_length=40)
	last_name               = models.CharField(max_length=40)
	date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin                = models.BooleanField(default=False)
	is_active               = models.BooleanField(default=True)
	is_staff                = models.BooleanField(default=False)
	is_superuser            = models.BooleanField(default=False)


	USERNAME_FIELD = 'identifiant'

	objects = MyAccountManager()

	def __str__(self):
		return self.identifiant

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True