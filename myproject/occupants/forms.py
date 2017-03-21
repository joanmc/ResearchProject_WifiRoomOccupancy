from django import forms
from .models import Rooms, Modules, Document
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)

	def clean_password(self):
		if self.data['password'] and self.data['confirm_password'] and (self.data['password'] != self.data['confirm_password']):
			raise forms.ValidationError("Passwords do not match")
		return self.data['password']

	class Meta:
		model = User
		fields = ['username', 'email' ,'password', 'confirm_password']

class UploadForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = "__all__"