from django.urls import path
from .views import UsersListView, UserDetailView, UserCreateView

urlpatterns = [
	path('users', UsersListView.as_view(), name='users-list'),
	path('user', UserCreateView.as_view(), name='user-create'),
	path('user/<str:uid>', UserDetailView.as_view(), name='user-detail'),
]