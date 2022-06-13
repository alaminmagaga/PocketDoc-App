from multiprocessing import context
from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):
    def get(self, request):
        context = {
            'title': 'Home'
        }
        return render(request, 'home.html')


class AppointmentView(View):
    def get(self, request):
        return render(request,'appointment.html')

    def post(self, request):
        context = {
            'sent': True
        }
        return render(request,'appointment.html', context)
