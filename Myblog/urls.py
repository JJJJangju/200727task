"""Myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

import blogapp.views
import profileapp.views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.main,name="main"),
    path('detail/<int:blog_id>',blogapp.views.detail,name="detail"),
    path('new/',blogapp.views.new,name="new"),
    path('create/',blogapp.views.create,name="create"),
    path('renew/<int:blog_id>',blogapp.views.renew,name="renew"),
    path('update/<int:blog_id>',blogapp.views.update,name="update"),
    path('delete/<int:blog_id>',blogapp.views.delete,name="delete"),
    path('profileapp/profile/',profileapp.views.profile,name="profile"),
    path('profileapp/upload/',profileapp.views.upload,name="upload"),
    path('profileapp/upload_create/',profileapp.views.upload_create,name="upload_create"),
    path('profileapp/upload_form/',profileapp.views.upload_form,name="upload_form"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)