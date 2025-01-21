from django.db import models

# Create your models here.
class PemainBola(models.Model):
    nama = models.CharField(max_length=100)
    posisi = models.CharField(max_length=50)
    klub = models.CharField(max_length=100)
    umur = models.IntegerField()

    def __str__(self):
        return self.nama