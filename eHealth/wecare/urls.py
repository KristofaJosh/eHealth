from django.urls import path
from .views import (
    user_register, 
    practitioner_register,
    index,
    dashboard,    
)

urlpatterns = [
    path('', index.Index.as_view(), name='index'),
    path('dashboard/', dashboard.Dashboard.as_view(), name='dashboard'),
    path('register/', user_register.UserFormView.as_view(), name='register'),
    path('practitioner/register', practitioner_register.practitioner_register, name='practitioner-register'),
]