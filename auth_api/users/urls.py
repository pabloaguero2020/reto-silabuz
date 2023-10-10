from django.urls import path
from .views import RegisterView, logout_view
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from . import views


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_jwt_token, name='login'),
    path('token-refresh/', refresh_jwt_token, name='token-refresh'),
    path('logout/', logout_view, name='logout'),
    path('verify-token/', views.verify_token, name='verify-token'),
]