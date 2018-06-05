from rest_framework import serializers


from visit.models import Visit



class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ('user','ip')