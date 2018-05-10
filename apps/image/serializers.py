from django.contrib.auth import get_user_model
from rest_framework import serializers

from image.models import Image

User = get_user_model()


class BlogImgSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.url

    class Meta:
        model = Image
        fields = ('user', 'url')


class BlogListImgSerializer(serializers.Serializer):
    imgs = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=True), write_only=True
    )
    blog_imgs = serializers.ListField(
        child=serializers.CharField(max_length=100000, ), read_only=True
    )

    def create(self, validated_data):
        imgs = validated_data.get('imgs')
        images = []
        for index, url in enumerate(imgs):
            image = Image.objects.create(url=url, user=User.objects.get(id=self.context['request'].user.id))
            blog = BlogImgSerializer(image, context=self.context)
            images.append(blog.data['url'])
        return {'blog_imgs': images}
