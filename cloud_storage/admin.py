from django.contrib import admin
from cloud_storage.models import storage,Image,Video,Audio,Document
# Register your models here.
admin.site.register(storage)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Document)
