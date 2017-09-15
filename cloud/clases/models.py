# @Author: Manuel Rodriguez <valle>
# @Date:   04-Sep-2017
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 12-Sep-2017
# @License: Apache license vesion 2.0


from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ClasesPreguntas(models.Model):
    nombre = models.CharField(max_length=50)
    modify = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.nombre


class Familias(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre



class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    promocion = models.DecimalField(decimal_places=2, max_digits=9, null=True, blank=True)
    precio = models.DecimalField(decimal_places=2, max_digits=9, null=True,  blank=True)
    color = models.CharField(max_length=10, default="#d898e8")
    orden = models.IntegerField(default=0)
    clasespreguntas = models.ManyToManyField(ClasesPreguntas, blank=True)
    modify = models.DateTimeField(auto_now=True)
    familias = models.ForeignKey(Familias, blank=True)
    ignore = models.CharField(max_length=150, blank=True, default="")

    def __unicode__(self):
        return u"{0} - tipo: {1}".format(self.nombre, self.familias.__unicode__())

    class Meta:
        ordering = ('orden', 'nombre', "familias")


class Ingredientes(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(decimal_places=2, max_digits=9, null=True, default=0.0)
    color = models.CharField(max_length=10, default="#d898e8")
    orden = models.IntegerField(default=0)
    productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
    modify = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('orden', 'nombre')




class Clases(models.Model):
    nombre = models.CharField(max_length=50)
    promocion = models.DecimalField(decimal_places=2, max_digits=9, null=True, blank=True)
    precio = models.DecimalField(decimal_places=2, max_digits=9, null=True,  blank=True)
    color = models.CharField(max_length=10, default="#d898e8")
    orden = models.IntegerField(default=0)
    productos = models.ManyToManyField(Productos,  blank=True)
    clasespreguntas = models.ManyToManyField(ClasesPreguntas,  blank=True)
    modify = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('orden', 'nombre')




class Preguntas(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(decimal_places=2, max_digits=9, null=True, default=0.0)
    color = models.CharField(max_length=10, default="#d898e8")
    orden = models.IntegerField(default=0)
    clasespreguntas = models.ForeignKey('ClasesPreguntas', on_delete=models.CASCADE)
    modify = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('orden', 'nombre')



class Sugerencias(models.Model):
    sugerencia = models.CharField(max_length=100)
    productos = models.ForeignKey('Productos', on_delete=models.CASCADE)
    def __unicode__(self):
        return self.sugerencia