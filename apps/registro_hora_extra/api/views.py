from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.registro_hora_extra.api.serializers import Registro_hora_extraSerializer
from apps.registro_hora_extra.models import Registro_hora_extra


class Registro_hora_extraViewSet(viewsets.ModelViewSet):
    queryset = Registro_hora_extra.objects.all()
    serializer_class = Registro_hora_extraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
