from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(null=False, blank=False,max_length=50, default="")
	last_name = models.CharField(null=False, blank=False,max_length=50, default="")
	mobile = models.CharField(null=False, blank=False, max_length=10, default="")
	address_1 = models.CharField(null=False, blank=False,max_length=200, default="")
	address_2 = models.CharField(blank=True,max_length=200, default="")
	state =  models.CharField(max_length=50, default="")
	city =  models.CharField(null=False, blank=False,max_length=50, default="")
	country =  models.CharField(null=False, blank=False,max_length=50, default="")
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __unicode__(self):
		return str(self.user.username)
