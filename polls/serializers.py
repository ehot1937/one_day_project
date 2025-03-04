from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'author', 'element', 'planet', 'incense',
            'candle', 'direction', 'source', 'sigil_url', 'appearance',
            'service', 'note', 'offering'
        ]
