from django.urls import path
from . import views

app_name = 'worksched'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('init/', views.InitView.as_view(), name='init'),
    path('set-pattern/<int:pk>', views.SetPatternView.as_view(), name='setpattern'),
    path('api/worksched/<int:year>/<int:month>', views.ApiView.as_view(), name='api'),
    path('worksched/<int:year>/<int:month>/image',
        views.getSchedWithImageView.as_view(), name='image'),
]
