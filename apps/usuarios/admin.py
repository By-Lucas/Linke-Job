from django.contrib import admin

from .models.models_user import ProfileUser, Escolaridade

admin.site.register(ProfileUser)
admin.site.register(Escolaridade)
