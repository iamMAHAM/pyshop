from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='client_accueil'),
    path('apropos', views.apropos, name='client_apropos'),
    path('contact', views.contact, name='client_contact'),
    path('boutique', views.boutique, name='client_boutique'),
    path('arrivage', views.arrivage, name='client_arrivage'),
    path('single-arrivage', views.single_arrivage, name='client_single_arrivage'),
    path('404', views.page_404, name='404')
]



