"""samplesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from .views import index, by_rubric,BbCreateView, add_and_save, BbDetailView     #add,add_save,


urlpatterns = [

         #path('admin/', admin.site.urls),
         path('bboard/', index),
        # path('bboard/', include('bboard.urls')),#don't work
         path('add/', BbCreateView.as_view(), name='add'),
         path('<int:rubric_id>/', by_rubric, name='by_rubric'),
         path('', index, name='index'),
         #path('add/save/', add_save, name='add_save'),
         #path('add/', add, name='add')
         path('add/save/', add_and_save, name='add_and_save'),
         path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
]


