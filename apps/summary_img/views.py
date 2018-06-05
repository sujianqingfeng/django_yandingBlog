from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from summary_img.models import SummaryImg
from summary_img.serializers import SummaryImgSeralizer
from utils.permission import IsOwnerOrReadOnly


class SummaryImgViewSet(viewsets.ModelViewSet):
    serializer_class = SummaryImgSeralizer

    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            return SummaryImg.objects.filter(user=self.request.user)
        else:
            return SummaryImg.objects.all()
