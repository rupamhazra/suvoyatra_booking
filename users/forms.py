from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Users

class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = Users
		fields = '__all__'