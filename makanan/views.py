from django.shortcuts import render, redirect, get_object_or_404
from .models import Makanan
from rest_framework.viewsets import ModelViewSet
from .serializers import MakananSerializer
# from django.http import JsonResponse
from django.contrib import messages
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.core.paginator import Paginator

class MakananViewSet(ModelViewSet):
    queryset = Makanan.objects.all()
    serializer_class = MakananSerializer

# HTML Form View
def makanan_form(request):
    makanan_id = request.GET.get('edit')  # Ambil ID dari parameter URL untuk edit
    if makanan_id:
        makanan = get_object_or_404(Makanan, id=makanan_id)
    else:
        makanan = None

    if request.method == 'POST':
        nama = request.POST.get('nama')
        harga = request.POST.get('harga')
        deskripsi = request.POST.get('deskripsi')

        # Validasi input
        if not nama or not harga or not deskripsi:
            messages.error(request, "Semua field harus diisi.")
            return redirect('makanan_form')

        if not harga.isdigit() or int(harga) <= 0:
            messages.error(request, "Harga harus berupa angka positif.")
            return redirect('makanan_form')

        if makanan:
            makanan.nama = nama
            makanan.harga = harga
            makanan.deskripsi = deskripsi
            makanan.save()
            messages.success(request, "Makanan berhasil diperbarui.")
        else:
            Makanan.objects.create(nama=nama, harga=harga, deskripsi=deskripsi)
            messages.success(request, "Makanan berhasil ditambahkan.")
        return redirect('makanan_form')

    makanan_list = Makanan.objects.all()
    # paginator = Paginator(makanan_list, 10)  # 10 item per halaman
    # page_number = request.GET.get('page')
    # makanan_page = paginator.get_page(page_number)
    return render(request, 'makanan/makanan_form.html', {'makanan_list': makanan_list, 'makanan': makanan})

def makanan_hapus(request, makanan_id):
    makanan = get_object_or_404(Makanan, id=makanan_id)
    makanan.delete()
    messages.success(request, "Makanan berhasil dihapus.")
    return redirect('makanan_form')

# @api_view(['GET'])
# def makanan_list_api(request):
#     makanan = Makanan.objects.all()
#     serializer = MakananSerializer(makanan, many=True)
#     return Response(serializer.data)