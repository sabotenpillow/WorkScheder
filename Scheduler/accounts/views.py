from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
#from .models import User
from .models import User
from .forms import UserUpdateForm

class SignUpView(generic.CreateView):
    #form_class    = UserCreationForm
    #success_url   = reverse_lazy('login')
    #template_name = 'accounts/signup.html'
    def dispatch(self, *args, **kwargs):
        return HttpResponse("not allowed")

class UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm

    #def post(self, request, *args, **kwargs):

