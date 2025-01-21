from django.shortcuts import render, redirect, get_object_or_404
from .models import PemainBola
from .serializers import PemainBolaSerializer
from rest_framework.viewsets import ModelViewSet

class PemainBolaViewSet(ModelViewSet):
    queryset = PemainBola.objects.all()
    serializer_class = PemainBolaSerializer

def pemainbola_form(request, pemainbola_id=None):
    if pemainbola_id:
        pemainbola = get_object_or_404(PemainBola, id=pemainbola_id)  # Ambil data berdasarkan ID untuk edit
    else:
        pemainbola = None  # Jika tidak ada ID, buat form baru

    if request.method == 'POST':
        nama = request.POST.get('nama')
        posisi = request.POST.get('posisi')
        umur = request.POST.get('umur')
        klub = request.POST.get('klub')
        if pemainbola:
            pemainbola.nama = nama
            pemainbola.posisi = posisi
            pemainbola.umur = umur
            pemainbola.klub = klub
            pemainbola.save()
        else:
            PemainBola.objects.create(nama=nama, posisi=posisi, umur=umur, klub=klub)
        return redirect('/api/pemainbola/form/')

    pemainbola_list = PemainBola.objects.all()
    return render(request, 'pemainbola/pemainbola_form.html', {'pemainbola_list': pemainbola_list, 'pemainbola': pemainbola})

# Fungsi untuk menghapus pemain bola
def pemainbola_hapus(request, pemainbola_id):
    pemainbola = get_object_or_404(PemainBola, id=pemainbola_id)
    pemainbola.delete()
    return redirect('/api/pemainbola/form/')  # Kembali ke halaman daftar pemain bola setelah dihapus
