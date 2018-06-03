
from  rest_framework import serializers

from summary_img.models import SummaryImg


class SummaryImgSeralizer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __str__(self):
        return self.url

    class Meta:
        model = SummaryImg
        fields = ('user', 'sumary_url')