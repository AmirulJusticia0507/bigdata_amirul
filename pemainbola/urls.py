from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PemainBolaViewSet, pemainbola_form, pemainbola_hapus

router = DefaultRouter()
router.register(r'pemainbola', PemainBolaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('form/', pemainbola_form, name='pemainbola_form'),  # Form baru
    path('form/<int:pemainbola_id>/', pemainbola_form, name='pemainbola_form'),  # Form untuk edit pemain bola
    path('hapus/<int:pemainbola_id>/', pemainbola_hapus, name='pemainbola_hapus'),  # Menambahkan URL untuk hapus
]
