from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib import messages


class LoginView(SuccessMessageMixin, auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            messages.error(self.request, f"""O usuário 
                        {self.request.user.first_name} 
                        {self.request.user.last_name}
                        já está logado """)
            return redirect(reverse_lazy("index"))
        else:
            login(self.request, form.get_user())
            messages.success(self.request, f"""Seja bem vindo(a) 
                            {self.request.user.first_name} 
                            {self.request.user.last_name}
                            """)
            return redirect(reverse_lazy("index"))


class LogoutView(auth_views.LogoutView):
    next_page = 'index'