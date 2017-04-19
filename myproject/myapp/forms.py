# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control','name':'username'})),
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name':'password'})),



class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
