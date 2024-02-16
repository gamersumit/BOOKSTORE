
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CustomUserSerializer
from .utils import AccountUtils
import json
from django.contrib.auth.hashers import check_password, make_password
from .models import CustomUser
from rest_framework.authtoken.models import Token
from bookstore.bs_utils import BookStoreUtils
# Create your views here.

class RegisterView(generics.CreateAPIView) :
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def post(self, request):
        try:
            # Convert base64_image to raw image if provided
            if 'image' in request.data:
                if 'image_name' not in request.data:
                    return Response({'status': False, 'message': 'image_name is required'}, status=400)

                image_base64 = request.data['image']
                image_name = request.data['image_name']
                image = BookStoreUtils.base64_to_image(image_base64, image_name)

                # Update request data with raw image
                request.data['image'] = image

            # Serialize data
            serializer = self.serializer_class(data=request.data, instance=self.get_object() if is_update else None)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            # Return response
            return Response({'status': True, 'message': 'User Registerd Succesfully'}, status=200)

        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status=400)
        

 # logout view // delete token       
class LogoutView(generics.RetrieveAPIView) :
    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Token '):
            token = auth_header.split(' ')[1]

            token = Token.objects.get(key = token)
            token.delete()
            return Response({'status': True, 'message': 'User Logout Successfully'}, status = 200)
        
        else :
            return Response({'status': False, 'message': 'Missing Token'}, status = 400)
        
# SHORT NAMING :
user_register_view = RegisterView.as_view()
user_logout_view = LogoutView.as_view()

