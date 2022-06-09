from django.db import models

class Clothes(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    bar_code = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'prenda'
        verbose_name_plural = 'prendas'


class Categoria(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        
class Size(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'talle'
        verbose_name_plural = 'talles'
        