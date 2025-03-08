from django.db import models

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    quantity = models.IntegerField('Quantidade')
    price = models.DecimalField('Preço', max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Produtos'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
