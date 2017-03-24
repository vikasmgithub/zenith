from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	location = models.CharField(max_length=240,blank=False,null=True)
	full_name = models.CharField(max_length=120,blank=True,null=True)
	# timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	# updated=models.DateTimeField(auto_now_add=False,auto_now=True)
	contact_no = models.CharField(max_length=240,blank=False,null=True)

	def __str__(self):
		return(self.email)