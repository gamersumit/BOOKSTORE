from rest_framework import generics
from bookstore.models import BookStore
from account.models import CustomUser
from .models import Cart
from .serializers import CartSerializer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token

class CartUpdateView(generics.GenericAPIView) :
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_class = [permissions.IsAuthenticated]

    def put(self, request) :
        try :
            # fetch user from request
            token = request.headers.get('Authorization').split()[1]
            token = Token.objects.get(key = token)
            user = token.user
            
            # add user inside request
            request.data['user'] = user.id

            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)

            # if item already exist
            if Cart.objects.filter(user = user,book = request.data['book']).exists() :
                cart_item = Cart.objects.get(user = user, book = request.data['book'])
                cart_item.quantity = request.data['quantity']
                cart_item.save()

                if cart_item.quantity <= 0 :
                        cart_item.delete()
            
            else :
                serializer.save()
            
            return Response({'status': True, 'message' : 'Book added Successfully'}, status =200)

        except Exception as e:
                return Response({'status': False, 'message' : str(e)}, status = 400)
      
class CartListAPIView(generics.ListAPIView):
    
    serializer_class = CartSerializer
    permission_class = [permissions.IsAuthenticated]
   
    def get_queryset(self):
        
        token = self.request.headers.get('Authorization').split()[1]
        token = Token.objects.get(key = token)
        user = token.user
        cartitem = Cart.objects.filter(user=user)
        return cartitem
    
class CartEmptyCartView(generics.GenericAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_class = [permissions.IsAuthenticated]
    
    def delete(self, request):
        try:
            token = request.headers.get('Authorization').split()[1]
            token = Token.objects.get(key = token)
            user = token.user

            # empty cart/ delte items from cart where user = request.user
            Cart.objects.filter(user=user).delete()
            return Response({'status': True, "message" : "cart items deleted successfully"}, status = 200)
         
        except Exception as e:
             return Response({'status': False, "message" : str(e)}, status = 400)


# #shortnaming
cart_update_view = CartUpdateView.as_view()
cart_list_view =  CartListAPIView.as_view()
cart_empty_view = CartEmptyCartView.as_view()