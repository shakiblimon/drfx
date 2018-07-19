from django.urls import path, include

urlpatterns = [
    path('user/',include('users.urls')),
    path('rest-auth/',include('rest_auth.urls')),
]