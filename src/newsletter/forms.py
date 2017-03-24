from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields=['location','email','full_name','contact_no']

	# def clean_email(self):
	# 	email=self.cleaned_data.get('email')
	# 	email_base,provider = email.split("@")
	# 	domain,extension = provider.split('.')
	# 	if not extension == "edu":
	# 		raise forms.ValidationError("please enter a vali .edu email address")
	# 	return email


	def clean_full_name(self):
		full_name=self.cleaned_data.get('full_name')

		return full_name

# class contactForm(forms.Form):
# 	full_name=forms.CharField(required=False);
# 	email=forms.EmailField();
# 	message=forms.CharField();

