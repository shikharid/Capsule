import json
from django.contrib.auth import authenticate, login, logout


from rest_framework import status, views, permissions, viewsets, mixins, generics
from rest_framework.response import Response
from authentication.models import User
from authentication.permission import IsAnonymous
from authentication.serializers import UserSerializer


class LoginView(views.APIView):

    permission_classes = [IsAnonymous]

    def post(self, request):

        try:
            data = json.loads(request.body)
            member_id = data.get('member_id', None)
            password = data.get('password', None)
            remember_me = data.get('remember_me', None)
            user = authenticate(member_id=member_id, password=password)
            if user:
                login(request, user)
                serialized_data = UserSerializer(user)
                if remember_me is None:
                    request.session.set_expiry(0)
                return Response(serialized_data.data)
            else:
                return Response({
                    'status': 'Not authorized',
                    'message': 'Invalid Login Details'
                }, status=status.HTTP_401_UNAUTHORIZED)
        except ValueError:
            return Response({
                    'status': 'Invalid Request',
                    'message': 'Invalid Request Paramaters'
                    }, status=status.HTTP_401_UNAUTHORIZED)




class LogoutView(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response({
            'status': 'Log Out',
            'message': 'Successfully Logged Out'
        }, status=status.HTTP_204_NO_CONTENT)


class UserDetailsView(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class UserLoginView(views.APIView):

    def get(self, request):
        return Response({'loggedIn': request.user.is_authenticated()})


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]