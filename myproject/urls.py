from django.urls import path
from Login.views import CustomLoginView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'), 
    path('login/', CustomLoginView.as_view(), name='login'),  
]
