# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token 

def logout_user(request):
	return render(request, 'accounts/logout.html')

def login_form(request):
	return render(request, 'accounts/login.html')

def get_auth_token(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, passwword=password)
	if user is not None:
		if user.is_active:
			token, created = Token.objects.get_or_create(user=user)
			request.session['auth'] = token.key
			return redirect('/cliente/', request)
	return redirect(settings.LOGIN_URL, request)


# Create your views here.
