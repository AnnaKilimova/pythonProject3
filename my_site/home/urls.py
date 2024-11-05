from django.urls import path, re_path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.home_view, name='home'),  # home/
    # http://127.0.0.1:8000/about/
    path('about/', views.about_view, name='about'),  # about/
    # http://127.0.0.1:8000/contact/
    path('contact/', views.contact_view, name='contact'),  # contact/

    # Динамічні маршрути
    # http://127.0.0.1:8000/post/123/
    re_path(r'^post/(?P<id>\d+)/$', views.post_view, name='post'),  # post/<id>/
    # http://127.0.0.1:8000/profile/john/
    re_path(r'^profile/(?P<username>\w+)/$', views.profile_view, name='profile'),  # profile/<username>/
    # http://127.0.0.1:8000/event/2024/08/15/
    re_path(r'^event/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.event_view, name='event'), # event/<year>/<month>/<day>/
]
