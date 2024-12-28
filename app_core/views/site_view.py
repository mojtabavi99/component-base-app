import json
from django.views import View
from django.shortcuts import render, redirect

from app_core.models import Province, City

class HomeView(View):
    def get(self, request):
        return render(request, 'app_core/home.html')
    
def mainHeaderComponent(request):
    return render(request, 'components/_main_header.html')


def mainFooterComponent(request):
    return render(request, 'components/_main_footer.html')
    