from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return HttpResponse("Ласкаво просимо на головну сторінку")

def about_view(request):
    return HttpResponse("Про нас")

def contact_view(request):
    return HttpResponse("Зв'яжіться з нами")

# Динамічні представлення
def post_view(request, id):
    return HttpResponse(f"Ви переглядаєте пост з ID: {id}")

def profile_view(request, username):
    return HttpResponse(f"Ви переглядаєте профіль користувача: {username}")

def event_view(request, year, month, day):
    return HttpResponse(f"Дата події: {year}-{month}-{day}")



# def home_view(request):f
#     return render(request, 'home/home.html')
#
# def about_view(request):
#     return render(request, 'home/about.html')
#
# def contact_view(request):
#     return render(request, 'home/contact.html')
#
# def post_view(request, id):
#     return render(request, 'home/post.html', {'id': id})
#
# def profile_view(request, username):
#     return render(request, 'home/profile.html', {'username': username})
#
# def event_view(request, year, month, day):
#     return render(request, 'home/event.html', {'year': year, 'month': month, 'day': day})


