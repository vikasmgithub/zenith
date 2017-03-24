# from django.conf import settings
# from django.core.mail import send_mail
from django.shortcuts import render

# from .forms import contactForm,SignUpForm


def home(request):
	# title = "Welcome"
#	if request.user.is_authenticated():
#		title = "My Title %s" %{request.user}
	# form =SignUpForm(request.POST or None)
	# context = {
	#      "title":title,
	#      "form":form,
	# }

	# if form.is_valid():
	# 	instance = form.save(commit=False)
	# 	instance.save()
	# 	context = {
	#      "title":"thank you",
	# }

	return render(request,"index.html",{})

def carpenter(request):

	return render(request,"carpenter.html",{})

def electrician(request):

	return render(request,"Electrician.html",{})

def wallpaint(request):

	return render(request,"wallpaint.html",{})

def plumber(request):

	return render(request,"plumber.html",{})

def laundry(request):

	return render(request,"laundry.html",{})

def automobile(request):

	return render(request,"automobile.html",{})