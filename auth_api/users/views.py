from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from .serializers import UserSerializer

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import logout

from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({'user': serializer.data, 'token': token})
        return Response(serializer.errors, status=400)



@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Successful logout"})

@api_view(['POST'])
@permission_classes([AllowAny])
def verify_token(request):
    token = request.data.get('token')
    data = {'token': token}
    try:
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        return Response({'token': valid_data['token']}, status=200)
    except:
        return Response({'error': 'Token is invalid or expired'}, status=400)