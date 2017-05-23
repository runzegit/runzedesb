from rest_framework import serializers
from .models import Cliente, Duplicata

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = '__all__'

class DuplicataSerializer(serializers.ModelSerializer):
	codClie = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), many=False, required=False)

	class Meta:
		model = Duplicata
		fields = '__all__'