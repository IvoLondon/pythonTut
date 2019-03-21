from django.urls import path
from basicform import views

app_name = 'basicform'

urlpatterns = [
    path('user/', views.form_name_view, name='register'),
    path('adminitrator/', views.form_admin_view, name='adminreg'),
]