from django.urls import path
from .views import login  # Make sure 'login' is imported

urlpatterns = [
    path('login/', login, name='login'),
]