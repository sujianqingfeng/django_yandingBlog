from rest_framework import serializers

from category.models import Category


class CategoryCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ('name', 'user', 'id')


class CategoryDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    update_time = serializers.DateField(read_only=True)
    add_time = serializers.DateField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
