from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('change-password/<int:pk>',
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/change_password.html',
            success_url=reverse_lazy('accounts:change-password-done')
        ),
        name='change-password'
    ),
    path('change-password/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='accounts/change_password_done.html'
        ),
        name='change-password-done'
    ),
]
