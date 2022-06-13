from django.urls import path
from . import views

urlpatterns = [
    path('',views.PredictionHomeView.as_view(),name='pred_home'),
    path('options',views.options,name='options'),
    path('diabetes',views.diabetes,name='diabetes'),
    path('predict2',views.predict2,name='predict2'),
    path('heart',views.heart,name='heart'),
    path('predict',views.predict,name='predict'),
    path('predict1',views.predict1,name='predict1'),
    path('liver',views.liver,name='liver'),
    path('kidney',views.kidney,name='kidney'),
    path('predict3',views.predict3, name='predict3'),
    path('brain',views.brain,name='brain'),
]