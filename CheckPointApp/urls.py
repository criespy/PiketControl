from django.urls import path
from . import views

urlpatterns = [
    path('checkpoint', views.CpInput.as_view(), name="CpInput"),
    path('report', views.Report.as_view(), name="CpReport"),
    path('login', views.PiketLoginView.as_view(), name="login"),
    path('logout', views.PiketLogoutView.as_view(), name="logout")
]
