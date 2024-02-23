from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from authentication.api.serializers import CustomUserSerializer
from authentication.models import CustomUser
from oauth2_provider.decorators import protected_resource
from django.utils.decorators import method_decorator
from oauth2_provider.models import RefreshToken

from customers.api.serializers import CustomerSerializer


class RegisterView(APIView):
 

    def post(self, request):
        user_serializer = CustomUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()

            # Extract user data to pass to CustomerSerializer
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'date_of_birth': user.date_of_birth,
            }

            # Add user data to request data before creating Customer
            request.data['user'] = user_data

            customer_serializer = CustomerSerializer(data=request.data)
            if customer_serializer.is_valid():
                customer_serializer.save()
                return Response({'detail': 'Registration successful'}, status=status.HTTP_201_CREATED)
            else:
                user.delete()  # Roll back user creation if Customer creation fails
                return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(protected_resource(), name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = CustomUser.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
