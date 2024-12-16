from django.views import View
from django.shortcuts import render, redirect

class HomeView(View):
    def get(self, request):
        return render(request, 'app_core/home.html')
    
def mainHeaderComponent(request):
    return render(request, 'components/_main_header.html')


def mainFooterComponent(request):
    return render(request, 'components/_main_footer.html')
    