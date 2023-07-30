"""drf2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from api import views

urlpatterns = [
    path('api/<str:version>/home/', views.HomeView.as_view(), name='hh'),
    path('api/<str:version>/img/', views.ImgView.as_view(), name='img'),
    path('api/<str:version>/depart/', views.DepartView.as_view(), name='depart'),
    path('api/<str:version>/user/', views.UserView.as_view()),
]
