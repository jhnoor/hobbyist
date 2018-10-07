from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from hobbyist.users import models, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from knox.models import AuthToken


class UserViewSet(viewsets.ViewSet):
    """
    API endpoint for users
    """

    def list(self, request):
        queryset = models.CustomUser.objects.filter(
            is_superuser=False).order_by('-kudos')
        serializer = serializers.CustomUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.CustomUser.objects.filter(is_superuser=False)
        user = get_object_or_404(queryset, pk=pk)
        serializer = serializers.CustomUserSerializer(user)
        return Response(serializer.data)


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.CustomUserSerializer

    def get_object(self):
        return self.request.user


class RegistrationAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = serializers.CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": serializers.CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })


class LoginAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": serializers.CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)
        })
