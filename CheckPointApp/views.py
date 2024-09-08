from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CpInputModel
from .forms import CpInputForm

redirect_authenticated_user = True

class PiketLoginView(LoginView):
    template_name = 'login.html'

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
