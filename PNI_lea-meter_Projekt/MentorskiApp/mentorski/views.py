from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('logout')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            status = form.data.get('status')
            
            if form.is_valid() and status != "none":
                form.save()
                email = form.cleaned_data.get('email')
                messages.success(request, 'Account was created for ' + email)

                return redirect('login')
			

        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('logout')
	else:
		if request.method == 'POST':
			email = request.POST.get('email')
			password =request.POST.get('password')

			user = authenticate(request, email=email, password=password)

			if user is not None:
				login(request, user)
				return redirect('upisni_list')
				
			else:
				messages.info(request, 'Email OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def upisniList(request):
	user = request.user
	upisani_predmeti = user.upisi_set.all()
	predmeti = Predmeti.objects.all()
	if(user.status == "izvanredni"):
		predmeti = predmeti.order_by('sem_izvanredni')
	if(user.status == "redovni"):
		predmeti = predmeti.order_by('sem_redovni')

	print(upisani_predmeti)
	context = {'predmeti':predmeti, 'upisani_predmeti':upisani_predmeti, 'student':user}
	return render(request, 'upisni_list.html', context)
