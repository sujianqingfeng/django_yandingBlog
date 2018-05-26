from rest_framework import viewsets,mixins,permissions


from review.models import Review
from review.serializers import ReviewCreationSerializer

class ReviewViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):

    serializer_class = ReviewCreationSerializer
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]


    def perform_create(self, serializer):
        parent_review = serializer.validated_data.get('parent')
        review = serializer.save(user=self.request.user, parent=parent_review)