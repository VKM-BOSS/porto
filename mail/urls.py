from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from mail import views
urlpatterns = [
    path('', views.homemail, name='mailhome'),
    path('Signup', views.signup, name='signupmail'),
    path('out',views.out,name='outmail'),
    path('sent/<slug:pk>/',views.senter,name='sent'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
