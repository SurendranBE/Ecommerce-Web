from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('controlpanel/', admin.site.urls),
    path('eadmin/', include('eadmin.urls')),
    path('category/', include('category.urls')),
    path('product/', include('product.urls')),
]
