from django.urls import path
from . import views

app_name = 'basicform'

urlpatterns = [
    path('user/', views.form_name_view, name='register'),
]