from django.urls import path
from . import views

app_name = 'worksched'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('init/', views.InitView.as_view(), name='init'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('api/worksched/<int:year>/<int:month>', views.ApiView.as_view(), name='api'),
]
