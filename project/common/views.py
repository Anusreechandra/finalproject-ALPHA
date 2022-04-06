import email
from urllib import request 
from django.shortcuts import render
from django.shortcuts import redirect
from common.models import Laborer,AppAdmin


# Create your views here.
def alpha(request):
    return render(request,'alpha.html')

def about(request):
    return render(request,'about.html')

def payment(request):
    return render(request,'payment.html')


def reg(request):
	msg=''
	if request.method == 'POST':
		name = request.POST['username']
		email =request.POST['email']
		password = request.POST['password']
		cpassword =request.POST['cpassword']
		email_exist = Laborer.objects.filter(email=email).exists()

		if not email_exist:
			new_reg = Laborer(name=name, email=email,password=cpassword)
			new_reg.save()
			msg = "registerd succesfully"

		
		else:
			msg = "email already exists"
	return render(request,'reg.html',{'msg':msg,}) 

def login(request):
	msg = ''
	if request.method =='POST':
		email = request.POST['email']
		password = request.POST['password']
		laborer_exist = Laborer.objects.filter(email=email,password=password).exists()
		admin_exist = AppAdmin.objects.filter(email=email,password=password).exists()

		if laborer_exist:
			laborer_data = Laborer.objects.get(email=email,password=password)
			request.session['laborer'] = laborer_data.id
			return redirect('laborer:laborer_home')

		if admin_exist:
			admin_data =AppAdmin.objects.get(email=email,password=password)
			request.session['admin'] = admin_data.id
			return redirect('alphadmin:admin')
		else:
			msg = "incorrect password or username"
		

	return render(request,'login.html',{'msg':msg,}) 	


# def login(request):
#     msg = ""
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']

#         laborer_exist = Laborer.objects.filter(email = email,password = password).exists()
#         admin_exist = AppAdmin.objects.filter(email = email,password = password).exists()


#         if laborer_exist:
#             laborer_data = Laborer.objects.get(email = email,password = password)
#             request.session['laborer'] = laborer_data.id
#             return redirect('laborer:laborer_home')
#         if admin_exist:
#             admin_data = AppAdmin.objects.get(email = email,password = password)
#             request.session['admin'] = admin_data.id
#             return redirect('alphadmin:admin')
#         else:
#             msg = 'Incorrect Password!'
#     return render(request,'login.html',{'msg':msg,})
   
    
	
	
	
	
	
	
	
	

