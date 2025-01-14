from django.shortcuts import render,get_object_or_404


from .models import Araba #araba modelini ekliyoruz

# Create your views here.

def home(request):
    arabalar=Araba.objects.all() #araba sınıfının içerisindeki tüm objeleri getir
    return render(request,'index.html',{"arabalar":arabalar}) # gelen request ve template i gönderiyoruz. birden fazla veri olduğu için sözlük ile gönderiyoruz


def detay(request,araba_id):
    araba=get_object_or_404(Araba,pk=araba_id)
    return render(request,'arac.html',{"araba":araba})