from django.shortcuts import render
from django.http import HttpResponse
from Nayeem.models import *

# Create your views here.

def Surana(request):
	return render(request,'index.html')

def Login(request):
	return render(request,'html_page.html')

def home(request):
	return render(request,'home.html')

def register(request):
	Rname = request.POST.get('name')
	Remail = request.POST.get('email')
	Rnum = request.POST.get('phone-number')
	Rpass = request.POST.get('password')
	Rcpass = request.POST.get('Cpassword')
	Rcity = request.POST.get('city')
	Redu = request.POST.get('qualification')
	Raim = request.POST.get('ambitions')
	Rhob = request.POST.get('hobbies')
	
	email_list = RegisterDetails.objects.values_list('Remail',flat=True)
	if Remail in email_list:
		email_check = RegisterDetails.objects.get(Remail=Remail)
		if Remail == email_check.Remail:
			return render(request,'html_page.html',{'error':'Already Registered Please Login'})				
	else:
		if Rpass == Rcpass:
			RegisterDetails(Rname=Rname,Remail=Remail,Rnum=Rnum,password=encript_binary(Rpass),Rcpass=encript_binary(Rcpass),Rcity=Rcity,Redu=Redu,Raim=Raim,Rhob=Rhob).save()
			return render(request,'html_page.html',{'error':'Registered Successfully'})
		else:
			return render(request,'index.html')

def login_check(request):
	lemail = request.POST.get('email')
	lpass = request.POST.get('password')
	email_list = RegisterDetails.objects.values_list('Remail',flat=True)
	if lemail in email_list:
		lemail_check = RegisterDetails.objects.get(Remail=lemail)
		if encript_binary(lpass) == lemail_check.password:
			name = lemail_check.Rname
			city = lemail_check.Rcity
			hobby = lemail_check.Rhob
			edu = lemail_check.Redu
			aim = lemail_check.Raim
			num = lemail_check.Rnum
			email = lemail_check.Remail
			return render(request,'home.html',{'name':name,'city':city ,'hobby':hobby,'edu':edu,'aim':aim,'num':num,'email':email})
		else:
			return render(request,'html_page.html',{'error':'Wrong Credentials'})
	else:
		return render(request,'html_page.html',{'error':'Not Registered'})

def encript_binary(request):
	secret_key="riyu"
	secret_string=''.join(str(ord(i)) for i in secret_key)
	password_encript=''.join(str(ord(j)) for j in request)
	encripted_password=password_encript+secret_string
	return encripted_password


def encript(val):
	val=val.replace('a','^_~!_^')
	val=val.replace('e','_^!~^_')
	val=val.replace('i','^_@#_^')
	val=val.replace('o','/_#@_/')
	val=val.replace('u','_/$$/_')
	return val

def decript(val):
	val=val.replace('^_~!_^','a')
	val=val.replace('_^!~^_','e')
	val=val.replace('^_@#_^','i')
	val=val.replace('/_#@_/','o')
	val=val.replace('_/$$/_','u')
	return val

