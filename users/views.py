from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .store import list_users, get_user, create_user, update_user, delete_user
from .serializers import UserCreateSerializer, UserUpdateSerializer

class UsersListView(APIView):
	def get(self, request):
		return Response(list_users())

class UserCreateView(APIView):
	def post(self, request):
		serializer = UserCreateSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = create_user(serializer.validated_data)
		return Response(user, status=status.HTTP_201_CREATED)

class UserDetailView(APIView):
	def get(self, _request, uid: str):
		user = get_user(uid)
		if not user:
			return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
		return Response(user)

	def patch(self, request, uid: str):
		serializer = UserUpdateSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = update_user(uid, serializer.validated_data)
		if not user:
			return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
		return Response(user)

	def delete(self, _request, uid: str):
		success = delete_user(uid)
		if not success:
			return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
		return Response(status=status.HTTP_204_NO_CONTENT)