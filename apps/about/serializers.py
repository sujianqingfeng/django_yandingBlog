from rest_framework import serializers

from about.models import About


class AboutSeializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = About
        fields = ('user','content')
