from django.urls import path,include
from eadmin import views

urlpatterns = [
    path('', views.login, name='login'),
    path('ajax-check', views.ajax_check, name='ajax_check'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('category/', include('category.urls')),
    path('product/', include('product.urls')),
]