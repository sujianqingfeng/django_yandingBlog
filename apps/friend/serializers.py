from rest_framework import serializers

from friend.models import Friend


class FriendCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


    def create(self, validated_data):
        return Friend.objects.create(is_delete=True,**validated_data)

    class Meta:
        model = Friend
        fields = ('user', 'link', 'desc', 'icon', 'title')



class FriendUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Friend
        # fields = ('user', 'link', 'desc', 'icon', 'title')

        fields = ('user', 'is_delete')
