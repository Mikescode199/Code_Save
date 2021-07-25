from django.urls import path, include
from .views import *
from .routers import *


urlpatterns = [
    path('Url_code_saved/', include(router.urls)),
]