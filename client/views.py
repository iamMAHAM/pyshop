from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'client/accueil.html')

def apropos(request):
    return render(request, 'client/apropos.html')

def contact(request):
    return render(request, 'client/contact.html')

def boutique(request):
    return render(request, 'client/boutique.html')

def arrivage(request):
    return render(request, 'client/arrivage.html')

def single_arrivage(request):
    return render(request, 'client/single-arrivage.html')

def page_404(request):
    return render(request, 'client/404.html')