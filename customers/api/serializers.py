from rest_framework import serializers

from authentication.api.serializers import CustomUserSerializer
from authentication.models import CustomUser
from customers.models import Customer



class CustomerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Use the CustomUserSerializer to represent the related user

    class Meta:
        model = Customer
        fields = ['id', 'name', 'code', 'phone_number', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        customer = Customer.objects.create(user=user, **validated_data)
        return customer