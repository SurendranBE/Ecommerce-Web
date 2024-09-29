from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add', views.add_category, name='add_category'),
    path('ajax-insert', views.ajax_insert, name='ajax_insert'),
    path('view', views.category_view, name='category_view'),
    path('edit/<int:id>', views.category_edit, name='category_edit'),
    path('ajax-edit/<int:id>', views.ajax_edit, name='ajax_edit'),
    path('active-category/<int:id>', views.active_category, name='active_category'),
    path('publish-category/<int:id>', views.publish_category, name='publish_category'),
    path('remove-image/<int:id>', views.remove_image, name='remove_image'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

