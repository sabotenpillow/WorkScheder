from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse

class SignUpView(generic.CreateView):
    #form_class    = UserCreationForm
    #success_url   = reverse_lazy('login')
    #template_name = 'accounts/signup.html'
    def dispatch(self, *args, **kwargs):
        return HttpResponse("not allowed")
