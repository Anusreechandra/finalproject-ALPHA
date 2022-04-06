from django.urls import URLPattern, path
from . import views

app_name='alphadmin'

urlpatterns = [
  
      path('',views.admin,name='admin'),
      path('admin_logout',views.admin_logout,name='admin_logout'),
   


]