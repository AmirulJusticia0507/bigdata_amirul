import logging
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Konfigurasi logging
logger = logging.getLogger(__name__)

@csrf_exempt  # Hanya gunakan ini jika CSRF tidak diaktifkan
def get_keycloak_token(request):
    # URL API Keycloak
    url = "http://localhost:8081/realms/bimtek/protocol/openid-connect/token"

    # Data autentikasi Keycloak
    data = {
        "client_id": "admin-bimtek",
        "client_secret": "if018e1IPBqaYO0fG4lj0oMO0hUjeqVB",
        "username": "adminbimtek@gmail.com",
        "password": "Admin12345",
        "grant_type": "password",
        "scope": "openid"
    }

    try:
        # Log aktivitas
        logger.info("Memulai permintaan token ke Keycloak...")

        # Kirim permintaan ke Keycloak
        response = requests.post(url, data=data)
        logger.info(f"Status code Keycloak: {response.status_code}")

        if response.status_code == 200:
            # Ambil response JSON
            tokens = response.json()

            # Log hasil token
            logger.debug(f"Access Token: {tokens.get('access_token')}")

            # Return ke frontend
            return JsonResponse({
                "success": True,
                "message": "Token berhasil diperoleh",
                "data": {
                    "access_token": tokens.get("access_token"),
                    "id_token": tokens.get("id_token"),
                }
            }, status=200)

        else:
            # Log error dari Keycloak
            logger.error(f"Error dari Keycloak: {response.text}")
            return JsonResponse({
                "success": False,
                "message": "Gagal mendapatkan token",
                "error": response.json()
            }, status=response.status_code)

    except Exception as e:
        # Log exception
        logger.exception("Kesalahan saat memanggil Keycloak API")
        return JsonResponse({
            "success": False,
            "message": "Terjadi kesalahan internal",
            "error": str(e)
        }, status=500)
