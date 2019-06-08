from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
        path('about', views.about,name='about'),
    path('usecase', views.usecase, name='usecase'),
    path('community', views.community, name='community'),
    path('roadmap', views.roadmap, name='roadmap'),

]
