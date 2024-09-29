from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password, check_password
import json
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta
from datetime import date

def login(request):
	if request.session.has_key('user_id'):
		user_id = request.session['user_id']
		username = request.session['username']
		username = username.capitalize()
		return redirect('/eadmin/dashboard')
	else:
		return render(request, 'eadmin/index.html')

def dashboard(request):
	if not request.session.has_key('user_id'):
		return redirect('/eadmin/')
	else:
		user_id = request.session['user_id']
		username = request.session['username']
		username = username.capitalize()
		return render(request, 'eadmin/dashboard.html')

def ajax_check(request):
	if request.session.has_key('username'):
		username = request.session['username']
		return redirect('/eadmin/dashboard')
	elif request.method == 'POST':
		username = request.POST.get("username", None)
		password = request.POST.get("password", None)
		user = authenticate(username = username, password = password)
		if user is not None:
			user_id = User.objects.get(username=username)
			request.session['username'] = username
			request.session['user_id'] = user_id.id
			return redirect('/eadmin/dashboard')
		else:
			messages.error(request, "Invalid Email or Password.")
			return redirect('/eadmin')
	return render(request, 'eadmin/index.html', {})

def logout(request):
	del request.session['username']
	del request.session['user_id']
	return redirect('/eadmin')