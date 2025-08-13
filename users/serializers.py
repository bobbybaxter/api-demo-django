from rest_framework import serializers

class UserCreateSerializer(serializers.Serializer):
	firstName = serializers.CharField(max_length=255)
	lastName = serializers.CharField(max_length=255, required=False, allow_blank=True)
	email = serializers.EmailField()
	phone = serializers.CharField(max_length=50, required=False, allow_blank=True)

class UserUpdateSerializer(serializers.Serializer):
	firstName = serializers.CharField(max_length=255, required=False)
	lastName = serializers.CharField(max_length=255, required=False)
	email = serializers.EmailField(required=False)
	phone = serializers.CharField(max_length=50, required=False)