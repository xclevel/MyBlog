from django import forms
#
# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
from .models import ckeditorBlog


class ckeditorForm(forms.ModelForm):
    class Meta:
        model = ckeditorBlog
        fields = ('title','content')