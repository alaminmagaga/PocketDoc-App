from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('index', views.index, name='home'),
    path('options',views.options,name='options'),
    path('appointment',views.appointment,name='appointment'),
    path('diabetes',views.diabetes,name='diabetes'),
    path('predict2',views.predict2,name='predict2'),
    path('heart',views.heart,name='heart'),
    path('predict',views.predict,name='predict'),
    path('predict1',views.predict1,name='predict1'),
    path('liver',views.liver,name='liver'),
    path('kidney',views.kidney,name='kidney'),
    path('predict3',views.predict3, name='predict3'),
    path('brain',views.brain,name='brain'),
    path('<str:username>/', views.chatPage, name='chat'),
]
