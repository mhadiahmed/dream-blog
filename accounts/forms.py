from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()
class CustomUserCreateForm(UserCreationForm):
	#finger_printe = forms.CharField(widget=forms.HiddenInput())
	class Meta:
		model = User
		fields = ('username','email')

	def __init__(self, *args, **kwargs):
		super(CustomUserCreateForm, self).__init__(*args, **kwargs)

		for fieldname in ['username','email', 'password1', 'password2']:
			self.fields[fieldname].help_text = None
