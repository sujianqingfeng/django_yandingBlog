from rest_framework import serializers

from about.models import About


class AboutSeializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    add_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = About
        fields = ('user','content','add_time')

