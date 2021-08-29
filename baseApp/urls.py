
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('Services/', views.services, name="services"),
    path('Skill/', views.skill, name="skill"),
    path('Contact/', views.contact, name="contact"),



   

]