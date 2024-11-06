from django.shortcuts import render

from django.shortcuts import render
from django.views import View

# Функціональні  відображення
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Класові відображення
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

class ServiceView(View):
    def get(self, request):
        # Список усіх послуг
        services = [
            {"name": "Веб-разработка", "description": "Создание веб-сайтов и приложений"},
            {"name": "SEO", "description": "Поисковая оптимизация"},
            {"name": "Маркетинг", "description": "Интернет-маркетинг и продвижение"},
            {"name": "Контент-маркетинг", "description": "Создание и продвижение контента"},
            {"name": "SMM", "description": "Продвижение в социальных сетях"},
        ]

        # Отримуємо значення з параметра 'search'
        search_query = request.GET.get('search', '').strip()

        # Фільтрація послуг на основі пошукового запиту
        if search_query:
            filtered_services = [
                service for service in services
                if search_query.lower() in service['name'].lower() or search_query.lower() in service['description'].lower()
            ]
        else:
            # Якщо немає пошукового запиту, показуємо всі послуги
            filtered_services = services

        # Передаємо відфільтрований список послуг у шаблон
        return render(request, 'services.html', {"filtered_services": filtered_services})