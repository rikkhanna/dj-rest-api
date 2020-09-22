from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
        """Serializes a field to test APIView"""
        name = serializers.CharField(max_length=10)
