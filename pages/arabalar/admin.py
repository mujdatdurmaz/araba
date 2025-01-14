from django.contrib import admin

# Register your models here.


from .models import Kategori,Araba

admin.site.register(Kategori)
admin.site.register(Araba)