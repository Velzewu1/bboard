from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/login/', views.BBLoginView.as_view(), name='login'),
    path('<str:page>', views.other_page, name='other'),
    path('', views.index, name='index')
]