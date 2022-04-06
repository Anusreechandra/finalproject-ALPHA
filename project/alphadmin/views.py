from urllib import request 
from django.shortcuts import redirect, render


# Create your views here.
def admin(request):
    return render(request,'admindashboard.html')

def admin_logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('common:login')