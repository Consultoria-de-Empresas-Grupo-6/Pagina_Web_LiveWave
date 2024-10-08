
from django.db import models #importa los metodos necesarios para trabajar con modellos
# Create your models here.




class Producto(models.Model):
    codigo_producto = models.CharField(max_length = 100,null=True, blank=True)  
    nombre_producto = models.CharField(max_length = 100,null=True, blank=True)  
    precio_producto = models.IntegerField(null=True, blank=True)
    stock_producto = models.IntegerField(null=True, blank=True)
    stock_minimo_producto = models.IntegerField(null=True, blank=True)
    stock_maximo_producto = models.IntegerField(null=True, blank=True)
    descripcion_producto = models.CharField(max_length = 100,null=True, blank=True)  
    
    imagen_producto = models.CharField(max_length=240, null=True, blank=True)
    estado_producto = models.CharField(max_length=100, null=True, blank=True, default='medio')

    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['stock_producto']
    #falta perfeccionar logica para caluclar estado
    def calcular_estado(self):
        if self.stock_producto <= self.stock_minimo_producto:
            self.estado_producto = 'bajo'

        if ((self.stock_producto >= self.stock_minimo_producto) and (self.stock_producto <= self.stock_maximo_producto)) :
            self.estado_producto = 'medio'
        else:
            self.estado_producto = 'alto'

    def __str__(self):
        return self.stock_producto


class Category_group(models.Model):
    category_group_name = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Category_group'
        verbose_name_plural = 'Category_groups'
        ordering = ['category_group_name']
    
    def __str__(self):
        return self.category_group_name

class Category(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, null=True)
    category_group = models.ForeignKey(Category_group, on_delete=models.CASCADE, default=2) 
    category_state = models.CharField(max_length=100, null=True, blank=True, default='Activa')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'
        ordering = ['producto__stock_producto']
    
    



