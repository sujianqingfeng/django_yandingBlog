from rest_framework import viewsets
from rest_framework import mixins


from review.models import Review
from review.serializers import ReviewSerializers

class ReviewViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):

    serializer_class = ReviewSerializers
    queryset = Review.objects.all()

