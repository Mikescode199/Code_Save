from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('codeuser.urls')),
    path('', include('api_code.urls')),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)