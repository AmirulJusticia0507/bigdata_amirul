from django.shortcuts import render, redirect, get_object_or_404
from .models import Makanan
from rest_framework.viewsets import ModelViewSet
from .serializers import MakananSerializer

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
        if makanan:
            makanan.nama = nama
            makanan.harga = harga
            makanan.deskripsi = deskripsi
            makanan.save()
        else:
            Makanan.objects.create(nama=nama, harga=harga, deskripsi=deskripsi)
        return redirect('makanan_form')

    makanan_list = Makanan.objects.all()
    return render(request, 'makanan/makanan_form.html', {'makanan_list': makanan_list, 'makanan': makanan})

def makanan_hapus(request, makanan_id):
    makanan = get_object_or_404(Makanan, id=makanan_id)
    makanan.delete()
    return redirect('makanan_form')
