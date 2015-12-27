from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render_to_response

def index(request):
	#user = User.objects.create_user('art', 'art@art.com', 'art')
	#user.save()
	context = {}
	populateContext(request, context)
	return render(request, 'index.html', context)

def login(request):
	context = {}
	try:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				populateContext(request, context)
				return render(request, 'loggedin.html', context)
			else:
				context['error'] = 'Non active user'
				populateContext(request, context)
				return render(request, 'index.html', context)
		else:
			context['error'] = 'Wrong username or password'
			return render(request,'index.html',context)
	except:
		context['error'] = ''
	return render(request,'index.html',context)

def loggedin(request):
	return render_to_response('loggenin.html',{'username':request.user.username})

def logout(request):
	context = {}
	try:
		auth_logout(request)
	except:
		context['error'] = 'Some error occured.'
	
	populateContext(request, context)
	return render(request, 'index.html', context)

def populateContext(request, context):
	context['authenticated'] = request.user.is_authenticated()#to limit access to pages for logged in users
	if context['authenticated'] == True:
		context['username'] = request.user.username

