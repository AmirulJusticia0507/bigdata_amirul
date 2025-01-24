from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MakananViewSet, makanan_form, makanan_hapus
# from .views import makanan_list_api

router = DefaultRouter()
router.register(r'makanan', MakananViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('form/', makanan_form, name='makanan_form'),
    path('hapus/<int:makanan_id>/', makanan_hapus, name='makanan_hapus'),
    # path('api/makanan-list/', makanan_list_api, name='makanan_list_api'),
]
