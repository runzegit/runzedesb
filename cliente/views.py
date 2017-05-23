# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Duplicata
from .serializers import ClienteSerializer, DuplicataSerializer
from django.contrib.auth.models import User
from rest_framework import permissions

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	permission_classes = (permissions.IsAuthenticated,)

class DuplicataViewSet(viewsets.ModelViewSet):
	queryset = Duplicata.objects.all()
	serializer_class = DuplicataSerializer
	permission_classes = (permissions.IsAuthenticated,)


# Create your views here.
