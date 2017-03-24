from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm

# def home(request):
# 	title = "Welcome"
# #	if request.user.is_authenticated():
# #		title = "My Title %s" %{request.user}
# 	form =SignUpForm(request.POST or None)
# 	context = {
# 	     "title":title,
# 	     "form":form,
# 	}

# 	if form.is_valid():
# 		instance = form.save(commit=False)
# 		instance.save()
# 		context = {
# 	     "title":"thank you",
# 	}

# 	return render(request,"home.html",context)

# def contactform(request):
# 	form=contactForm(request.POST or None)
# 	if form.is_valid():
# 		# for key in form.cleaned_data:
# 		# 	print (key)
# 		# 	print (form.cleaned_data.get(key))
# 		form_email=form.cleaned_data.get("email")
# 		form_message=form.cleaned_data.get("message")
# 		form_full_name=form.cleaned_data.get("full_name")

# 		subject='site contact form'
# 		from_email=settings.EMAIL_HOST_USER
# 		to_email= [from_email,'vikas.mundra57@gmail.com']
# 		contact_message="%s:%s via %s"%(
# 			form_full_name,
# 			form_message,
# 			form_email)

# 		send_mail(subject,
# 			contact_message,
# 			from_email,
# 			to_email,
# 			fail_silently=False)

# 	context = {
# 	"form":form,
# 	}
# 	return render(request,"forms.html",context)


# from django.conf import settings
# from django.core.mail import send_mail
#from django.shortcuts import render

#from .forms import contactForm,SignUpForm


def home(request):

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

def register(request):

	title = "Welcome"
	if request.user.is_authenticated():
		title = "My Title %s" %{request.user}
	form =SignUpForm(request.POST or None)
	context = {
	     "title":title,
	     "form":form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		context = {
	     "title":"thank you",
	}

	return render (request,"register.html",context)


