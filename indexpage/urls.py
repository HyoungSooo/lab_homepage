"""lab_homepage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.index, name='index'),
    path('about_professor', views.about_professor, name='about_professor'),
    path('what_we_do', views.what_we_do, name='what_we_do'),
    path('introduce', views.introduce, name='introduce'),
    path('pubilcation', views.pubilcation, name='pubilcation'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('post-detail/<int:post_id>',
         views.post_detail, name='post-detail'),
    path('others', views.others, name='others'),
]
