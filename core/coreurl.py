from . import views
from django.urls import path

from core.views.loginview import home
from core.views.loginview import login


urlpatterns = [
    path('', views.loginview.home, name='home'),
    path('login/', views.loginview.login, name="login"),
    path('signup/', views.loginview.signup, name="signup"),
]
