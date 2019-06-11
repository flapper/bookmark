"""bookmark URL Configuration

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
from django.urls import path, include, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from bookmark.models import Bookmark
from bookmark.views import BookmarkCreateView

app_name="bookmark"

urlpatterns = [
    path('', ListView.as_view(model=Bookmark, paginate_by=5), name="index"),
    path('add/', BookmarkCreateView.as_view(), name="add"),
    path('delete/<int:pk>/', DeleteView.as_view(model=Bookmark, success_url=reverse_lazy('bookmark:index')), name="delete",),
    path('detail/<int:pk>', DetailView.as_view(model=Bookmark), name="detail"),
]
