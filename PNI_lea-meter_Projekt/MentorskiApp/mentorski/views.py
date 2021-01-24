from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .decorators import *

@unauthenticated_user
def registerPage(request):
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


@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			if request.user.role=="student":
				return redirect('upisni_list', user.id)
			if request.user.role=="mentor":
				return redirect('predmeti')
		else:
			messages.info(request, 'Email OR password is incorrect')
	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@allowed_users(allowed_roles=["student","mentor"])
def upisniList(request, sk):
	user = request.user
	if user.role == "mentor":
		user = Korisnici.objects.get(id=sk)
	
	upisani_predmeti = user.upisi_set.all()
	u = upisani_predmeti.values('predmet')
	neupisani_predmeti = Predmeti.objects.exclude(upisi__predmet__in=u).distinct()
	predmeti = Predmeti.objects.filter(upisi__predmet__in=u).distinct()
	
	if(user.status == "izvanredni"):
		predmeti = predmeti.order_by('sem_izvanredni')
	if(user.status == "redovni"):
		predmeti = predmeti.order_by('sem_redovni')

	context = {'neupisani_predmeti':neupisani_predmeti, 'upisani_predmeti':upisani_predmeti,'predmeti':predmeti, 'student':user}
	return render(request, 'upisni_list.html', context)


@allowed_users(allowed_roles=["student","mentor"])
def upis(request,pk,sk):
	form = UpisForm(initial={'predmet':pk,'student':sk})
	predmet = Predmeti.objects.get(kod=pk)
	if request.method == 'POST':
		form = UpisForm(request.POST,initial={'predmet':pk,'student':sk})
		if form.is_valid():
			form.save()
			return redirect('upisni_list', sk)
	context = {'form':form, 'predmet':predmet, 'student_id':sk}
	return render(request, 'upis.html', context)


@allowed_users(allowed_roles=["student","mentor"])
def izbrisiUpis(request,pk,sk):
	upis = Upisi.objects.get(predmet_id=pk, student_id=sk)
	predmet = Predmeti.objects.get(kod=pk)
	student = Korisnici.objects.get(id=sk)
	if request.method == "POST":
		upis.delete()
		return redirect('upisni_list', student.id)
	context = {'predmet':predmet, 'student':student}
	return render(request, 'upis_izbrisi.html', context)


@allowed_users(allowed_roles=["student","mentor"])
def statusUpis(request,pk,sk):
	predmet = Predmeti.objects.get(kod=pk)
	student = Korisnici.objects.get(id=sk)
	upis = Upisi.objects.get(predmet_id=pk, student_id=sk)
	
	print(upis.status)
	if request.method == "POST":
		
		if upis.status == "položeno":
			upis.status = "nepoloženo"
			upis.save()
		elif upis.status == "nepoloženo":
			upis.status = "položeno"
			upis.save()
		print(upis.status)
		return redirect('upisni_list', student.id)
	context = {'predmet':predmet, 'student':student,'upis':upis}
	return render(request, 'upis_status.html', context)


@allowed_users(allowed_roles=["mentor"])
def predmeti(request):
	predmeti = Predmeti.objects.all()
	context = {'predmeti':predmeti}
	return render(request, 'predmeti.html', context)


@allowed_users(allowed_roles=["mentor"])
def predmetUredi(request,pk):
	predmet = Predmeti.objects.get(kod=pk)

	form = PredmetForm(instance=predmet)
	if request.method == 'POST':
		form = PredmetForm(request.POST, instance=predmet)
		if form.is_valid():
			form.save()
			return redirect('predmeti')

	context = {'form':form}
	return render(request, 'predmet_uredi.html', context)


@allowed_users(allowed_roles=["mentor"])
def predmetDodaj(request):
	form = PredmetForm()
	if request.method == 'POST':
		form = PredmetForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('predmeti')

	context = {'form':form}
	return render(request, 'predmet_uredi.html', context)


@allowed_users(allowed_roles=["mentor"])
def studenti(request):
	studenti= Korisnici.objects.filter(role="student")

	context = {'studenti':studenti}
	return render(request, 'studenti.html', context)