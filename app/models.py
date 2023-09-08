from django.db import models
from datetime import datetime


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    description = models.CharField(max_length=350, verbose_name='Descripción', null=True, blank=True)

    def __str__(self):
        return "Categoria: {}".format(self.name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    category = models.ForeignKey("Category", verbose_name="Categoría", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img/productos/', null=True, blank=True, verbose_name='Imagen')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return "Nombre producto: {}".format(self.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']


class Client(models.Model):
    # categorys = models.ManyToManyField("Category", verbose_name="Categoría")
    # type = models.ForeignKey("Type", on_delete=models.CASCADE) #tambien se puede models.SET_NULL para setear un nulo, pero debe tener el null=True activado, tambien models.PROTECT para evitar que se borre una tabla con registros de otra
    name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellido')
    dni = models.CharField(max_length=10, unique=True, verbose_name='DNI')
    date_created = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Fecha de creacion')  # auto_now_add=True toma la fecha actual cuando se crea el registro
    date_update = models.DateTimeField(auto_now=True,
                                       verbose_name='Fecha de actualizacion')  # auto_now=True toma la fecha de actualizacion
    sexo = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return "Nombres: {}, DNI: {}".format(self.name, self.dni)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['id']  # forma ascendente si lo quiere de forma descendente colocar - antes de id: -id


class Sale(models.Model):
    cliente = models.ForeignKey("Client", verbose_name="Cliente", on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    sub_total = models.DecimalField("Subtotal", default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField("IVA", default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField("Total", default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return "Venta: {}, Fecha: {}".format(self.cliente, self.date_joined)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']  # forma ascendente si lo quiere de forma descendente colocar - antes de id: -id


class DetailSale(models.Model):
    sale = models.ForeignKey("Sale", verbose_name="venta", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", verbose_name="Producto", on_delete=models.CASCADE)
    price = models.DecimalField("Precio", default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField("Cantidad", default=0.00)
    sub_total = models.DecimalField("Subtotal", default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return "Venta: {}, Producto: {}".format(self.sale, self.producto)

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle Ventas'
        ordering = ['id']  # forma ascendente si lo quiere de forma descendente colocar - antes de id: -id
