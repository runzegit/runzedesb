# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cliente(models.Model):
	nomClie =  models.CharField(max_length=60)
	cpf = models.CharField(max_length=11)
	email = models.CharField(max_length=60)
	diasBlo = models.IntegerField()
	datVen = models.DateField()
	datCad = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Cliente"
		verbose_name_plural = "Clientes"

	def __unicode__(self):
		return self.nomClie 

class Duplicata(models.Model):
	numDocto = models.CharField(max_length=10)
	codClie = models.ForeignKey('Cliente')
	datEmi = models.DateField()
	datVen = models.DateField()
	valDocto = models.DecimalField(max_digits=10, decimal_places=2)
	datPag = models.DateField()
	valJuro = models.DecimalField(max_digits=10, decimal_places=2)
	valDesc = models.DecimalField(max_digits=10, decimal_places=2)
	valPago = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		verbose_name = "Duplicata"
		verbose_name_plural = "Duplicatas"

	def __unicode__(self):
		return self.numDocto 



# Create your models here.
