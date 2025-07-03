from django.urls import path

from core import views


app_name = 'core'
urlpatterns = [
    path('', views.base, name='base'),
    path('main/', views.main, name='main'),
    path('main/<slug:slug>/', views.specified_project, name='specified_project'),
]