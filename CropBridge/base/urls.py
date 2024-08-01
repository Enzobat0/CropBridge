from .views import *
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', landingPage, name='landingPage'),
    path('home/', homeView, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('new-product/', saveProduct, name='newProduct'),
    path('delete-product/<str:pk>', deleteProduct, name='deleteProduct'),
    path('details/<str:pk>', detailsView, name='details'),
    path('update-product/<str:pk>', ProductUpdateView.as_view(), name='updateProduct'),
]

urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)