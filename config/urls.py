from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

def homepage(_request):
    return JsonResponse({'message': 'API Demo - Django'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('', include('users.urls')),
]
