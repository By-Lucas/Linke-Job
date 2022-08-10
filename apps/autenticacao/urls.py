from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views.views_auth import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
