from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('about/', views.about, name='about'),  # Added trailing slash
    path('form/', views.form, name='form'),     # Added trailing slash
]
