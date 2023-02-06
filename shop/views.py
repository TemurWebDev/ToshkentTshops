from django.shortcuts import render
from .models import CategoryProduct,Category,Banner,Maxsus,About

# Create your views here.

def index(request):
    banner = Banner.objects.all()
    category_BestSellers = CategoryProduct.objects.filter(category__category_name='BestSellers')
    category_Featured = CategoryProduct.objects.filter(category__category_name='Featured')
    category_NewArrival = CategoryProduct.objects.filter(category__category_name='NewArrival')
    category_Aksesuar = CategoryProduct.objects.filter(category__category_name='Aksesuar')
    category = Category.objects.all()

    maxsus = Maxsus.objects.all()

    about = About.objects.all()



    return render(request,'index.html',
                  {'banner':banner,
                    'category_BestSellers':category_BestSellers,
                   'category_Featured':category_Featured,
                   'category_NewArrival':category_NewArrival,
                   'category_Aksesuar':category_Aksesuar,
                   'category':category,
                   'maxsus':maxsus,
                   'about':about,
                   })
