from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, name='initial_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('experiences/', views.getExperiences),
    path('athletes/', views.getAthletes)
]