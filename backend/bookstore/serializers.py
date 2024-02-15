from rest_framework import serializers
from .models import BookStore



class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStore
        fields = ['id', 'title', 'author', 'price', 'publication_year', 'image']

    
    def validate_Price(self, value):
        if not value :
            raise serializers.ValidationError("Price is required")
        
        else :
            if(value < 0) :
               raise serializers.ValidationError("Price cannot be negative")
            return value