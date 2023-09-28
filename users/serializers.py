from rest_framework.fields import SerializerMethodField
from rest_framework import serializers as szs

from users.models import (
    User,
    DiscountCard,
    FeedBack
)


class UserListSerializer(szs.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(szs.ModelSerializer):
    message = SerializerMethodField()
    password = szs.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'message'
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def get_message(self, obj):
        return (
            'Verification message has been sent to your email, please verify your email.'
        )


class UserManageSerializer(szs.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]


class UserVerifySerializer(szs.ModelSerializer):
    token = szs.CharField(max_length=555)

    class Meta:
        model = User
        fields = [
            'token'
        ]


class DiscountCardSerializer(szs.ModelSerializer):
    class Meta:
        model = DiscountCard
        fields = '__all__'


class FeedBackListSerializer(szs.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'


class FeedBackCreateSerializer(szs.ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = FeedBack
        fields = [
            'user',
            'title',
            'content',
            'review'
        ]

    def get_user(self, obj):
        return self.context['request'].user.id
