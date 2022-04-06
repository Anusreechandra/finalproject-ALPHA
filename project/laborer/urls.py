from django.urls import URLPattern, path
from . import views

app_name='laborer'

urlpatterns = [
  
    path('laborer_home',views.profile,name="laborer_home"),
    path('qwe',views.qwe,name="qwe"),
    path('laborer_logout',views.laborer_logout,name='laborer_logout')
    


]