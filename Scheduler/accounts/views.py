from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import UserUpdateForm

class SignUpView(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('worksched:login')
    template_name = 'accounts/signup.html'
    #def dispatch(self, *args, **kwargs):
    #    return HttpResponse("not allowed")

class PasswordUpdateView(PasswordChangeView, generic.UpdateView):
    template_name = 'accounts/change_password.html'
    model         = User
    #form_class    = PasswordChangeForm
    #success_url   = reverse_lazy('worksched:index')
