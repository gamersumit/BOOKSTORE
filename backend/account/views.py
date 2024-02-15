
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .utils import AccountUtils
import json
from django.contrib.auth.hashers import check_password, make_password
from .models import CustomUser
# Create your views here.

class RegisterView(generics.CreateAPIView) :
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
        

# SHORT NAMING :
user_register_view = RegisterView.as_view()

