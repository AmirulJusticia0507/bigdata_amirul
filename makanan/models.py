from django.db import models

# Create your models here.
class Makanan(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama