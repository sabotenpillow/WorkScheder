from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('init/', views.InitView.as_view(), name='init'),
    path('api/worksched/<int:year>/<int:month>', views.ApiView.as_view(), name='api'),
]
