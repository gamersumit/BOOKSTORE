from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import BookStoreSerializer
from .models import BookStore
from account.permissions import AdminPermissions
from rest_framework import permissions
from . bs_utils import BookStoreUtils
# Create your views here.
  
class BookStoreViewSet(viewsets.ModelViewSet):
    queryset = BookStore.objects.all()
    serializer_class = BookStoreSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [permissions.IsAuthenticated, AdminPermissions]  # Only authenticated users can create, update, partial_update, or delete
        else:
            permission_classes = [permissions.IsAuthenticated]  # All users are allowed for other actions (e.g., retrieve, list)
        
        return [permission() for permission in permission_classes]
    

    def create(self, request, *args, **kwargs):
        return self.save_book(request, is_update=False)

    def update(self, request, *args, **kwargs):
        return self.save_book(request, is_update=True)

    def save_book(self, request, is_update=False):
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
            message = 'Book updated Successfully' if is_update else 'Book added Successfully'
            return Response({'status': True, 'message': message}, status=200)

        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status=400)