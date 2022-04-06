from django.urls import URLPattern, path
from . import views

app_name='common'

urlpatterns = [
  
    path('',views.alpha,name='alpha'),
    path('reg',views.reg,name='reg'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    # path('admin',views.login,name='admin'),
    path('payment',views.payment,name='payment'),
    


]