# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import login as auth_login, logout as auth_logout
from rest_framework.authtoken.models import Token 
from django.contrib.auth.models import User

def logout_user(request, *args, **kwargs):
	kwargs['next_page'] = 'accounts:login_form'
	return auth_logout(request, *args, **kwargs)
	
def login_form(request, *args, **kwargs):
	if request.user.is_authenticated():
		return redirect('clientes:cliente_list')
	kwargs['extra_context'] = {'next':'/cliente/'}
	kwargs['template_name'] = 'accounts/login.html'
	return auth_login(request, *args, **kwargs)

def get_auth_token(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, passwword=password)
	if user is not None:
		if user.is_active:
			auth_login(request, user)
			token, created = Token.objects.get_or_create(user=user)
			request.session['auth'] = token.key
			#return redirect('/cliente/', request)
			return render(request, 'accounts/error.html', {'error': 'Login inválido 3'})
	return redirect('accounts/error.html', request)


# Create your views here.
