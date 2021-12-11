from django.db.models import fields
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from tours.models import Tour, Zona, User 

# def index(request):
#     tours = Tour.objects.all()

#     return render (request, 'index.html', {'tours': tours})

from rest_framework import viewsets, serializers  

from .models import Zona, Tour


@login_required()
def index(request):
    """ Vista para atender la petición de la url / """
    # Obteniendo los datos mediantes consultas
    tours = Tour.objects.all()
    zonas = Zona.objects.all()

    return render(request, "index.html", {"tours":tours, "zonas":zonas})


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializador para poder atender las conversiones para USER"""

    class Meta:
        #Se define sobre que modelo actua y define la propiedade del "serializador"

        model = User 

        # Se define los campos a incluir y ponerlos tal cual se registraron en "models.py"

        fields = ('id', 'name', 'last_name', 'email', 'birthday', 'genre', 'key', 'type')


class UserViewSet(viewsets.ModelViewSet): 
    queryset= User.objects.all().order_by('id')  #COMO VAN A OPERAR MIS DATOS, UNA FORMA DE TRABAJAR CON BASES DE DATOS y SE USA EL ORM 

    serializer_class = UserSerializer   #Esto es para exponer los datos y se tiene que crear uno 


# curl -d '{'name': 'Donald', 'last_name': 'Mac Pato', 'email': 'donald@disney.com', 'birthday': '10-01-01', 'genre': 'H'}' -H Content-Type: application/json' htttp://localhost:8000/api/users/


class TourSerializer(serializers.HyperlinkedModelSerializer):  # ¡¡¡¡¡NOTA: AQUI SE SUBIO ESTE "SERIALIZER YA QUE ESTABA ABAJO Y TE AVISABA QUE EL "TourSerializer" no existia, esa es la razón por la cual se subio

    class Meta:

        model = Tour 

        fields = ('name', 'slug', 'operator', 'type', 'description', 'img', 'pais', 'zonaSalida', 'zonaLlegada')



class ZonaSerializer(serializers.HyperlinkedModelSerializer):

    tours_salida = TourSerializer(many=True, read_only = True)  #En lugar de traer la data con URLs, puedo traer algo que me represente esto con los datos de un "tour" para no tener el recurso solo con una URL 

    class Meta:

        model = Zona

        fields = ('nombre', 'descripcion', 'latitud', 'longitud', 'tours_salida', 'tours_llegada')  #Aqui se agrego tour salida, para listar dentro de cada tour y zona "cuales son los tours que existen por que tienen su zona de salida o de llegada "


class ZonaViewSet(viewsets.ModelViewSet): 
    queryset= Zona.objects.all().order_by('id')  

    serializer_class = ZonaSerializer  #También se tiene que cambiar aqui el "serializador"



class TourViewSet(viewsets.ModelViewSet): 
    queryset= Tour.objects.all().order_by('id')  

    serializer_class = TourSerializer  #También se tiene que cambiar aqui el "serializador"


