from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from cloud_storage import views
from cloud_storage.views import DetailImage,DetailVideo,DetailAudio,DetailDocument,Detailinter,Deletefile
urlpatterns = [
    path('', views.homecloud, name='home'),
    path('Signup', views.signup, name='signup'),
    path('out',views.out,name='out'),
    path('image/<slug:pk>/',views.image_upload,name='img'),
    path('video/<slug:pk>/',views.video_upload,name='vid'),
    path('audio/<slug:pk>/',views.audio_upload,name='aud'),
    path('document/<slug:pk>/',views.document_upload,name='doc'),
    path('detail/<slug:pk>/', DetailImage.as_view(), name='detail'),
    path('detailvid/<slug:pk>/', DetailVideo.as_view(), name='detailvid'),
    path('detailaud/<slug:pk>/', DetailAudio.as_view(), name='detailaud'),
    path('detaildoc/<slug:pk>/', DetailDocument.as_view(), name='detaildoc'),
    path('detailin/<slug:pk>/', Detailinter.as_view(), name='detailin'),
    path('delete/<slug:pk>/', Deletefile.as_view(), name='delete'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
