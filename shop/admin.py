from django.contrib import admin
from .models import CategoryProduct,Category,Banner,Maxsus,About

# Register your models here.
admin.site.register(Banner)
admin.site.register(CategoryProduct)
admin.site.register(Category)
admin.site.register(Maxsus)
admin.site.register(About)
