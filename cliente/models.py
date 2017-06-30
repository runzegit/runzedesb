# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Cliente(models.Model):
	nomClie =  models.CharField(verbose_name = "Nome", max_length=60)
	cnpj = models.CharField(verbose_name = "CNPJ", max_length=14)
	telefone = models.CharField(verbose_name = "Email", max_length=60, blank=True, null=True)
	datDesb = models.DateField(verbose_name = "Último Desbloqueio", blank=True, null=True)
	datPag = models.DateField(verbose_name = "Data Últ. Pag.", blank=True, null=True)
	mesRef = models.IntegerField(verbose_name = "Mês Referência", blank=True, null=True)
	diaVen = models.IntegerField(verbose_name = "Dia Vencimento", blank=True, null=True)
	bloqueado = models.BooleanField(verbose_name = "Bloqueado")
	ativo = models.BooleanField(verbose_name = "Ativo")

	class Meta:
		verbose_name = "Cliente"
		verbose_name_plural = "Clientes"

	def __unicode__(self):
		return self.nomClie 



# Create your models here.
