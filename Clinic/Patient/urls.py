from django.urls import path
from .import views
urlpatterns=[
    path('home',views.home,name='home'),
    path('login',views.login,name='plogin'),
    path('about',views.about,name='pabout'),
    path('register',views.register,name='pregister'),
    path('logout',views.logout,name="logout"),
    path('Heptities',views.hepatitisdata,name='Heptities'),
    path('form',views.form,name='form'),
    path('predict',views.predict,name='predict'),
    path('contact',views.contact,name='pcontact'),
    path('doctor',views.doctor,name="doctor"),
    path('welcome',views.welcome,name="welcome")

]