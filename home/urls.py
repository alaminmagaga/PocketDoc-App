from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('appointment',views.AppointmentView.as_view(),name='appointment'),
]
