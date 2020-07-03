from django.db import models

# Create your models here.

class Direccion (models.Model):
    calle = models.CharField(max_length = 30)
    ciudad = models.CharField(max_length = 30)
    numero = models.CharField(max_length = 30)
    def __str__(self):
        return '{}'.format(self.calle)

class Categoria(models.Model):
    nombre = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 50)
    def __str__(self):
        return '{}'.format(self.nombre)
        
class Proveedor (models.Model):
    nombre = models.CharField(max_length = 20)
    rut = models.IntegerField()
    telefono = models.CharField(max_length = 50)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    web = models.CharField(max_length=40)
    def __str__(self):
        return '{}'.format(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=35)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    provedoor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio = models.CharField(max_length=15)
    stock = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre

class Detalle (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad=models.CharField(max_length=15)
    def __str__(self):
        return '{}'.format(self.producto)
    
class Cliente(models.Model):
    rut = models.IntegerField()
    nombre = models.CharField(max_length = 20)
    telefono = models.CharField(max_length = 25)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)

class Venta(models.Model):
    fecha = models.DateField()
    detalle = models.ManyToManyField(Detalle)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.CharField(max_length = 20)
    def __str__(self):
        return '{}'.format(self.monto)

    
