from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog import views
from blog.views import Detail,createcomment,Commentupdate,Commentdelete,Postupdate,Postdelete
urlpatterns = [
    path('', views.homeblog, name='homeblog'),
    path('Signup', views.signup, name='signupblog'),
    path('outblog',views.out,name='outblog'),
    path('normal/<slug:pk>/',views.normalblog,name='normal'),
    path('image/<slug:pk>/',views.imgblog,name='image'),
    path('video/<slug:pk>/',views.vidblog,name='video'),
    path('audio/<slug:pk>/',views.audblog,name='audio'),
    path('Document/<slug:pk>/',views.Docblog,name='document'),
    path('detailblog/<slug:pk>/', Detail.as_view(), name='detailblog'),
    path('createcomment/<slug:pk>/<slug:opk>/', views.createcomment, name='cc'),
    path('editcomment/<slug:pk>/', Commentupdate.as_view(), name='ec'),
    path('deletecomment/<slug:pk>/', Commentdelete.as_view(), name='dc'),
    path('Postupdate/<slug:pk>/', Postupdate.as_view(), name='pu'),
    path('Postdelete/<slug:pk>/', Postdelete.as_view(), name='pd'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
