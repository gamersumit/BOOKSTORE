from rest_framework import serializers
from .models import Cart
from account.models import CustomUser
from bookstore.models import BookStore
from bookstore.serializers import BookStoreSerializer

class CartSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(write_only = True, queryset=CustomUser.objects.all())
    book = serializers.PrimaryKeyRelatedField(write_only = True, queryset=BookStore.objects.all())
    book_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'book', 'quantity', 'book_details']
    
    def get_book_details(self, obj):
        # Assuming you have a method in your Inventory model to get details
        product = BookStore.objects.get(id=obj.book.id)
        serializer = BookStoreSerializer(product)
        return serializer.data