from django.urls import path
from administracao.views.views_admin import Admin, Delete

urlpatterns = [
    path('', Admin.as_view(), name='admin'),
    path('delete/<int:pk>/', Delete.as_view(), name='Delete')
]