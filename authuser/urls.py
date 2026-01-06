from django.urls import path
from . import views

app_name='authuser'

urlpatterns = [
    path('login',views.LoginView.as_view(),name='login'),
    path('logout',views.logout,name='logout'),
    path('test_url',views.test_url,name='test_url'),
]
