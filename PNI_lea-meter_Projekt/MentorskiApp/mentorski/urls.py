from django.urls import path
from . import views

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('upisni_list/<str:sk>/', views.upisniList, name='upisni_list'),
    path('upis/<str:pk>/<str:sk>/', views.upis, name='upis'),
    path('upis_izbrisi/<str:pk>/<str:sk>/', views.izbrisiUpis, name='upis_izbrisi'),
    path('upis_status/<str:pk>/<str:sk>/', views.statusUpis, name='upis_status'),
    path('predmeti', views.predmeti, name='predmeti'),
    path('predmet_uredi/<str:pk>/', views.predmetUredi, name='predmet_uredi'),
    path('predmet_novi', views.predmetDodaj, name='predmet_novi'),
    path('studenti', views.studenti, name='studenti'),
]