from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('global_map/', views.global_map, name='global_map'),
    path('test_output/', views.test_output, name='test_output'),
    path('create_marker/', views.create_marker, name='create_marker'),
    path('logout/', views.logout_view, name='logout')
]
