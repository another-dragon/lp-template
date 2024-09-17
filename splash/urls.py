from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash_page, name='splash_page'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('home/<int:user_id>/', views.home_page, name='home_page'),
]