from django.shortcuts import render, redirect, HttpResponse
from .models import Dashboard 
from .forms import DasboardForm

# Create your views here.
def index(request):
    return render (request, 'LandingPage/index.html')

def sobre(request):
    return render (request, 'LandingPage/sobre.html')

def parceiros(request):
    return render (request, 'LandingPage/parceiros.html')

def experiencias(request):
    return render (request, 'LandingPage/experiencias.html')

def acelera(request):
    return render (request, 'LandingPage/acelera.html')

def contato(request):
    return render (request, 'LandingPage/contato.html')

def registra(request):
    return render (request, 'dashboard/login.html')

def user(request):
    return render (request, 'dashboard/user.html')

def login(request):
    return render (request, 'dashboard/login.html')

def analytic(request):
    return render (request, 'dashboard/Analytic.html')

def dashboard(request):
    return render (request, 'dashboard/dashboard.html')

def dashboard(request):
    dados = {
         'dados': Dashboard.objects.all()
    }
    return render(request, 'usuario/dashboard.html', context=dados)

def detalhe(request, id_dashboard):
    dados = {
        'dados': Dashboard.objects.get(pk=id_dashboard)                    
    }
    return render(request, 'usuario/dashboard.html', dados)


def criar(request):
    if request.method == 'POST':
        dashboard_form = DasboardForm(request.POST)
        if dashboard_form.is_valid():
            dashboard_form.save()
        return redirect('dashboard')    
    else:
        dashboard_form = DasboardForm()
        formulario = {
            'formulario': dashboard_form
        }
        return render(request, 'usuario/nova_compra.html', context=formulario)


def editar(request, id_dashboard):
    dashboard = Dashboard.objects.get(pk=id_dashboard)
    if request.method == 'GET':
        formulario = DasboardForm(instance=dashboard)
        return render(request, 'dashboard/login.html', {'formulario': formulario})
    else:
        formulario = DasboardForm(request.POST, instance=dashboard)
        if formulario.is_valid():
            formulario.save()
        return redirect('dashboard')    


def excluir(request, id_dashboard):
    dashboard = Dashboard.objects.get(pk=id_dashboard)
    if request.method == 'POST':
        dashboard.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/confirmar_exclusao.html', {'item': dashboard})  