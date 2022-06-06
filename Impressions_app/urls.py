from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('create_marker/', views.create_marker, name='create_marker'),
    path('logout/', views.logout_view, name='logout')
]
