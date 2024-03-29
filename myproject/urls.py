# Login/urls.py

from django.urls import path
from ..Login.views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    # Add more URL patterns for other views as needed
]
