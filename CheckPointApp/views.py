from django.views.generic import TemplateView, ListView, FormView
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

class CpInput(TemplateView):
    #login_url = 'login'
    model = CpInputModel
    template_name = 'cp_input.html'
    #form_class = CpInputForm
    success_url = '/success/' 

    def form_valid(self, form):
        # Process the form data
        form.save()
        return super().form_valid(form)


class Report(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = CpInputModel
