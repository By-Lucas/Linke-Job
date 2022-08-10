from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views.views_user import SignUpView, profileView, ProfileUpdateView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('profile/', profileView.as_view(), name='profile'),
    path('update-profile/', ProfileUpdateView.as_view(), name='update-profile')
]
