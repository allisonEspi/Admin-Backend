from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer,TCategoriaSerializer,TComentarioSerializer,TEscaneosSerializer,TFavoritoSerializer,TGaleriaSerializer,TLocalSerializer,TNotificacionesSerializer,TPermisoSerializer,TRolSerializer,TRolpermisoSerializer,TTelefonoSerializer,TUsuarioSerializer
from .models import Categoria,Comentario,Escaneos,Favorito,Galeria,Local,Notificaciones,Permiso,Rol,Rolpermiso,Telefono,Usuario
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = TCategoriaSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = TComentarioSerializer

class EscaneosViewSet(viewsets.ModelViewSet):
        queryset = Escaneos.objects.all()
        serializer_class = TEscaneosSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
        queryset = Favorito.objects.all()
        serializer_class = TFavoritoSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
        queryset = Galeria.objects.all()
        serializer_class =TGaleriaSerializer
class LocalViewSet(viewsets.ModelViewSet):
        queryset = Local.objects.all()
        serializer_class = TLocalSerializer
class NotificacionesViewSet(viewsets.ModelViewSet):
        queryset = Notificaciones.objects.all()
        serializer_class = TNotificacionesSerializer
class PermisoViewSet(viewsets.ModelViewSet):
        queryset = Permiso.objects.all()
        serializer_class = TPermisoSerializer
class RolViewSet(viewsets.ModelViewSet):
        queryset = Rol.objects.all()
        serializer_class = TRolSerializer
class RolpermisoViewSet(viewsets.ModelViewSet):
        queryset = Rolpermiso.objects.all()
        serializer_class = TRolpermisoSerializer
class TelefonoViewSet(viewsets.ModelViewSet):
        queryset = Telefono.objects.all()
        serializer_class = TTelefonoSerializer
class UsuarioViewSet(viewsets.ModelViewSet):
        queryset = Usuario.objects.all()
        serializer_class = TUsuarioSerializer