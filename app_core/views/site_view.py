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
    
    
# def importProvince(request):
#     with open('province.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)

#         for province_data in data:
#             Province.objects.create(
#                 name=province_data['name'],
#             )
#     print("Provinces imported successfully!")


# def importCity(request):
#     with open('city.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)

#         for city_data in data:
#             province_name = city_data['province_id']
#             province = Province.objects.get(pk=province_name)
#             if province:
#                 City.objects.create(
#                     name=city_data['name'],
#                     province=province
#                 )
#     print("Cities imported successfully!")
