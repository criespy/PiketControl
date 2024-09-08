from django.urls import path
from . import views

urlpatterns = [
    path('', views.CpInput.as_view(), name="CpInput"),
    path('report/', views.Report.as_view(), name="CpReport"),
    path('login/', views.PiketLoginView.as_view(), name="login"),
    path('logout/', views.PiketLogoutView.as_view(), name="logout"),
    path('success/<int:pk>/', views.Success.as_view(), name="success"),
]
