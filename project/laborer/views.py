import email
from urllib import request 
from django.shortcuts import redirect, render


# Create your views here.
def profile(request):
    return render(request,'profile.html')

def qwe(request):
    return render(request,'1.html')

def laborer_logout(request):
    del request.session['laborer']
    request.session.flush()
    return redirect('common:login')