from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from visit.models import Visit
from visit.serializers import VisitSerializer
from utils.request import get_ip_address_from_request

User = get_user_model()

class VisitViewSet(viewsets.GenericViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    @action(methods=['get'],detail=True)
    def visit(self,request,pk=None):
        user = User.objects.get(id=pk)
        if user:
            ip = get_ip_address_from_request(request)
            # Visit.objects.filter(ip=ip,add_time=)
            is_exist=Visit.objects.get_this_day().filter(ip=ip)
            if not is_exist:
                instance = Visit.objects.create(user=user,ip=ip)
                serializer = self.get_serializer(data=instance)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        return Response(status=status.HTTP_200_OK)

