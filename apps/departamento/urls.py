from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.views_departamento import (
    DepartamentoList, 
    DepartamentoUpdate, 
    DepartamentoCreate,
    DepartamentoDelete
    )

urlpatterns = [
    path('list/', DepartamentoList.as_view(), name='list_departamento'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentoUpdate.as_view(), name='update_departamento'),
    path('delete/<int:pk>', DepartamentoDelete.as_view(), name='delete_departamento'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)