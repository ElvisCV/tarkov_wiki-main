from django.db import models

class Weapon(models.Model):
    # 5 atributos obligatorios
    name = models.CharField(max_length=200, verbose_name="Nombre del Arma")
    description = models.TextField(verbose_name="Descripción")
    img = models.ImageField(upload_to='weapons/', verbose_name="Imagen del Arma")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")
    
    class Meta:
        verbose_name = "Arma"
        verbose_name_plural = "Armas"
        ordering = ['-created']
    
    def __str__(self):
        return self.name