from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import RegisterView, ActivationView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('activate/<uuid:activation_code>/', ActivationView.as_view(), name='activation'),
]
