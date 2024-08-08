from rest_framework_mongoengine import serializers
from kilimo_guard.models import *


class UsersSerializer(serializers.DocumentSerializer):

    class Meta:
        model = Users
        # fields = "__all__"
        exclude = ("password",)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        # Remove make_password and let the model handle password hashing
        return super(UsersSerializer, self).create(validated_data)
