from django.urls import path
from users.views import *

urlpatterns = [
    path('user-list/', UserListAPIView.as_view(), name='user-list'),
    path('user-create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user-verify/', UserVerifyAPIView.as_view(), name='user-verify'),
    path('user-manage/<int:pk>', UserManageAPIView.as_view(), name='user-manage'),

    path('d_card-list/', DiscountCardListAPIView.as_view(), name='d_card-list'),

    path('feedback-list/', FeedBackListAPIView.as_view(), name='feedback-list'),
    path('feedback-create/', FeedBackCreateAPIView.as_view(), name='feedback-create'),
]
