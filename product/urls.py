from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add', views.add_product, name='add_product'), 
    path('ajax-insert', views.ajax_insert, name='ajax_insert'),
    path('view', views.product_view, name='product_view'),
    path('edit/<int:id>', views.product_edit, name='product_edit'),
    path('ajax-edit/<int:id>', views.ajax_edit, name='ajax_edit'),
    path('active-product/<int:id>/', views.active_product, name='active_product'),
    path('available-product/<int:id>/', views.available_product, name='available_product'),
    path('remove-image/<int:id>', views.remove_image, name='remove-image'),
 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)