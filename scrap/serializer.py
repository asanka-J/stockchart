from rest_framework import serializers
from .models import Post


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("last_updated","price_usd")
        #fields = "__all__"
    
