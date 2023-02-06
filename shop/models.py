from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.title




class Category(models.Model):
    category_name = models.CharField(max_length=50)


    def __str__(self):
        return self.category_name



class CategoryProduct(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)


    def __str__(self):
        return self.name


class Maxsus(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class About(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField(upload_to='images/')



