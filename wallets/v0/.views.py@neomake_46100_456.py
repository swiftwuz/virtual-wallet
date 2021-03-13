from rest_framework import generics, status
from rest_framework.response import Response

from . serializers import UserSerializer


class RegisterUserView(generics.GenericAPIView):
    serialier_class = UserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serialier_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)
