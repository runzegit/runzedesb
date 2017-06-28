from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404, redirect
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from rest_framework.response import Response
from .models import Cliente
from .forms import ClienteForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q
from django.template import Context, loader
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from random import *


@csrf_exempt
@login_required(login_url='accounts:login_form')
def cliente_list(request):
	if request.method=='POST':
		cliente = get_object_or_404(Cliente, pk=request.POST.get('cliente_id'))
		form = ClienteForm(instance=cliente)
		return render(request, 'cliente/cliente_detail.html', {'form': form, 'cliente_id': cliente.id})	
			#return HttpResponse(html)
	else:
		clientes = Cliente.objects.all()[:10]
		return render(request, 'cliente/cliente_list.html', {'clientes': clientes})

@csrf_exempt
@login_required(login_url='accounts:login_form')
def cliente_busca(request):
	if request.method=='POST':
		clientes = Cliente.objects.filter(
			Q(nomClie__icontains=request.POST.get('busca')) | Q(cnpj__icontains=request.POST.get('busca'))
		)[:10]
		return render(request, 'cliente/cliente_list_lateral.html', {'clientes': clientes})

@csrf_exempt
@login_required(login_url='accounts:login_form')
def cliente_desb(request):
	clientes = Cliente.objects.all()
	return render(request, 'cliente/cliente_desb.html', {'clientes': clientes})

@csrf_exempt
@login_required(login_url='accounts:login_form')
def cliente_desb_busca(request):
	if request.method=='POST':
		clientes = Cliente.objects.filter(
			Q(nomClie__icontains=request.POST.get('busca')) | Q(cnpj__icontains=request.POST.get('busca'))
		)
		return render(request, 'cliente/linhas_clientes.html', {'clientes': clientes})

@csrf_exempt
@login_required(login_url='accounts:login_form')
def cliente_bloqueado(request):
	if request.method=='POST':
		if request.POST.get('status'):
			cliente = Cliente.objects.get(pk=request.POST.get('id'))
			cliente.ativo = not cliente.ativo
			cliente.save()
			return HttpResponse(cliente.ativo)
		elif request.POST.get('pagamento'): 
			cliente = Cliente.objects.get(pk=request.POST.get('id'))
			cliente.datPag = request.POST.get('data')
			cliente.mesRef = request.POST.get('mes')
			cliente.save()
			datePF = datetime.strptime(cliente.datPag, "%Y-%m-%d").strftime("%d de %B de %Y")
			return JsonResponse({'id': cliente.id, 'datPagF': datePF, 'datPag': cliente.datPag, 'mesRef': cliente.mesRef})
		else:
  			cliente = Cliente.objects.get(pk=request.POST.get('id'))
  			cliente.bloqueado = not cliente.bloqueado
			cliente.save()
			return HttpResponse(cliente.bloqueado)

@login_required(login_url='accounts:login_form')
def cliente_new(request):
	if request.method == "POST":
		form = ClienteForm(request.POST)
		if form.is_valid():
			cliente = form.save(commit=False)
			cliente.save()
			return redirect('clientes:cliente_list')
	else:
		form = ClienteForm()	
	return render(request, 'cliente/cliente_detail.html', {'form': form})

@login_required(login_url='accounts:login_form')
def cliente_edit(request, pk):
	cliente = get_object_or_404(Cliente, pk=pk)
	duplicatas =  Duplicata.objects.filter(codClie=cliente)
	if request.method == "POST":
		form = ClienteForm(request.POST, instance=cliente)
		if form.is_valid():
			cliente = form.save(commit=False)
			cliente.save()
			return redirect('clientes:cliente_list')
	else:
		form = ClienteForm(instance=cliente)	
	return render(request, 'cliente/cliente_detail.html', {'form': form, 'duplicatas': duplicatas})

@login_required(login_url='accounts:login_form')
def cliente_delete(request, pk):
	cliente = get_object_or_404(Cliente, pk=pk)
	cliente.delete()
	return redirect('clientes:cliente_list')

@csrf_exempt
@api_view(['POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
def cliente_api(request):
	if request.method == 'POST':
		status = request.data['status']
		parse = status.split('|')
		cnpj = parse[0]
		cliente = get_object_or_404(Cliente, cnpj=cnpj, ativo=False)
		_check = parse[3]
		check = _check[:-1]
		_indice =parse[3]
		indice = int(_indice[len(parse[3])-1:])
		if indice < 2:
			_check = int(check) - indice - int("{:%Y%m%d}".format(datetime.now()))
			impares = [3, 5, 7, 9]
			pares = [2, 4, 6, 8]
			if (int(_check) % 2 == 0 and indice == 0) or (int(_check) % 2 != 0 and indice == 1):
				if int(_check) % 2 == 0:
					if cliente.bloqueado:
						indice = impares[randint(0,3)]
					else:
						indice = pares[randint(0,3)]
				else:
					if cliente.bloqueado:
						indice = pares[randint(0,3)]
					else:
						indice = impares[randint(0,3)]
				items = ['BLOQUEADO', 'DESBLOQUEADO']
				status = items[randint(0,1)]
				mes = "{:%m}".format(datetime.now())
				data = int("{:%Y%m%d}".format(datetime.now()))
				numero = randint(100000000,999999999)
				codigo = data+numero+int(indice)
				resultado = cnpj+'|'+status+'|mes'+mes+'|'+str(codigo)+str(indice)
				resultadoJ = {"resultado":resultado}
				return JsonResponse(resultadoJ)
			else:
			    content = {"erro no codigo":"chave de verificacao invalida"}
			    return Response(content, status=status.HTTP_404_NOT_FOUND)
		else:
			cliente.bloqueado = True
			cliente.datDesb = datetime.now()
			cliente.save()
		   	content = {"status":"ok"}
			return Response(content, status=200)

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	#permission_classes = (permissions.IsAuthenticated,)



# Create your views here.
