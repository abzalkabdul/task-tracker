from django.urls import path

from core import views


app_name = 'core'
urlpatterns = [
    path('', views.base, name='base'),
    path('kanban_template/<slug:slug>/', views.kanban_template, name='kanban_template'),
]