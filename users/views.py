import jwt
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework_simplejwt.tokens import RefreshToken
from config.settings import SECRET_KEY
from users.models import (
    User,
    DiscountCard,
    FeedBack
)
from users.serializers import (
    UserListSerializer,
    UserCreateSerializer,
    UserManageSerializer,
    UserVerifySerializer,
    DiscountCardSerializer,
    FeedBackListSerializer,
    FeedBackCreateSerializer
)
from users.utils import UserVerifyMixin


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateAPIView(
    GenericAPIView
):
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user)
            current_site = request.get_host()
            link = reverse('user-verify')
            url = 'http://' + current_site + link + '?token=' + str(token)
            body = 'Hi!' + ' Use the link below to verify your email:\n' + url
            data = {
                'email_subject': 'Verify your email',
                'email_body': body,
                'to_email': user.email
            }
            UserVerifyMixin.send_mail(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserVerifyAPIView(GenericAPIView):
    serializer_class = UserVerifySerializer

    def get(self, request):
        token = request.GET.get('token')
        payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        user = User.objects.get(id=payload['user_id'])
        try:
            if not user.is_active:
                user.is_active = True
                user.save()
                return Response(
                    {'user': 'Successfully verified'}, status=status.HTTP_200_OK
                )
        except jwt.ExpiredSignatureError:
            return Response(
                {'error': 'Activation expired'}, status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.exceptions.DecodeError:
            return Response(
                {'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST
            )


class UserManageAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserManageSerializer


class DiscountCardListAPIView(ListAPIView):
    queryset = DiscountCard.objects.all()
    serializer_class = DiscountCardSerializer


class FeedBackListAPIView(ListAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackListSerializer


class FeedBackCreateAPIView(CreateAPIView):
    serializer_class = FeedBackCreateSerializer
