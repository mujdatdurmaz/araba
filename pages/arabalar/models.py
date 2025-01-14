from django.db import models

# Create your models here.


class Kategori(models.Model):
    isim=models.CharField(max_length=150) #kısa metin
    aciklama=models.TextField(null=True,blank=True) #uzun metin
    #veri null olabilir. giriş zorunlu değil.
    #bu python kodu tek başına sql tablosu oluşturamaz

    class Meta:
        verbose_name_plural="Araç Kategorileri"


    def __str__(self):
        return self.isim


class Araba(models.Model):
    isim=models.CharField(max_length=200)
    yil=models.IntegerField()
    fiyat=models.FloatField()
    kategori=models.ForeignKey(Kategori,on_delete=models.CASCADE)
    resim=models.ImageField(upload_to="images")
    motorhacmi=models.IntegerField(verbose_name="Araç Motor Hacmi")

    class Meta:
        verbose_name_plural="Arabalar"

    def __str__(self):
        sonuc = self.isim + " " + str(self.yil)
        return sonuc

