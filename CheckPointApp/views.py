from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CpInputModel
from .forms import CpInputForm
from django.contrib.auth import login, logout, authenticate
from django_auth_ldap.backend import LDAPBackend
from django.shortcuts import redirect
from django.contrib import messages

redirect_authenticated_user = True

class PiketLoginView(LoginView):
    template_name = 'login.html'
    success_url = '/'  # Replace with your desired success URL

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and self.request.user.is_active:
            return redirect(self.success_url)  # Redirect to the home page if already authenticated
            
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        # First try LDAP authentication
        ldap_backend = LDAPBackend()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = None
        try:
            user = ldap_backend.authenticate(self.request, username=username, password=password)
        except ldap.LDAPError as e:
            # Set an error message
            print(f"LDAP authentication error: {e}")
            pass

        # If LDAP authentication fails, fall back to the default model backend
        if user is None:
            user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(self.get_success_url())
        else:
            # Add an error message and return the invalid form
            return self.form_invalid(form)
        
    def form_invalid(self, form):
        # Set an error message
        messages.error(self.request, 'Login failed. Please check your username and password!')
        # Redirect to the dashboard or any other view
        # return redirect(reverse('dashboard_view'))  # Replace 'dashboard' with your actual dashboard view name
        return super().form_invalid(form)

class PiketLogoutView(LogoutView):
    def logout_view(selfrequest):
        logout(request)
    template_name = 'login.html'
    next_page = 'login'

class CpInput(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = CpInputModel
    template_name = 'cp_input.html'
    fields = '__all__'
    #form_class = CpInputForm
    #success_url = '/success/' 

class Success(DetailView):
    model = CpInputModel
    template_name = 'success.html'


class Report(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = CpInputModel
    template_name = 'report.html'
