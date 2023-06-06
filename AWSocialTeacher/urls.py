from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'AWST'
admin.site.index_title = ''

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_page'),
    path('', include('user.urls'), name='user'),
    path('students/', include('students.urls'), name='students'),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
