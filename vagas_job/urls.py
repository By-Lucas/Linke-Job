from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('core.urls')),
    path("vagas/", include('vagas.urls')),
    path("auth/", include('autenticacao.urls')),
    path("usuario/", include('usuarios.urls')),
    path("departamento/", include('departamento.urls')),
    #path("empresa/", include('empresas.urls')),
    #path("vaga/", include('vagas.urls')),
    #path("funcionario/", include('funcionarios.urls')),
    #path("candidato/", include('candidaturas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)