from rest_framework_mongoengine import serializers
from kilimo_guard.models import *

class UsersSerializer(serializers.DocumentSerializer):
    model = Users
    class Meta:
        model = Users  
        fields="__all__"