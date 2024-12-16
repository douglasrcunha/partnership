"""
URL configuration for partnership project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))



"""
from django.contrib import admin
from django.urls import path
from app import views
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.index, name='index'), 
    path('sobre/', views.sobre, name='sobre'), 
    path('parceiros/', views.parceiros, name='parceiros'), 
    path('experiencias/', views.experiencias, name='experiencias'), 
    path('acelera/', views.acelera, name='acelera'), 
    path('contato/', views.contato, name='contato'),     
    path('registra/', views.registra, name='registra'), 
    path('login/', views.login, name='login'), 
    path('user/', views.user, name='user'), 
    path('analytic/', views.analytic, name='analytic'), 
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('nova_compra/', views.criar, name='novo'),    
    path('nova_compra/<int:id_usuario>', views.editar, name='editar'),    
    path('excluir_usuario/<int:id_usuario>', views.excluir, name='excluir'),    
    path('<int:id_usuario>', views.detalhe, name='detalhe') ,
  
]
