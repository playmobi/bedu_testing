
from graphene_django import DjangoObjectType 

from tours.models import User, Zona, Tour, Salida 

import graphene  #MUY IMPORTANTE HACER ESTE IMPORT 


class UserType(DjangoObjectType): #Esta clase viene de "graphene"
    class Meta:
        model = User  #No olvidar hacer el import de arriba con: from tours.models import User 


class ZonaType(DjangoObjectType): 
    class Meta:
        model = Zona  # No olvidar que también se INTEGRA EN LA PARTE DEL "IMPORT" como: Zona


class TourType(DjangoObjectType): 
    """ Tipo de dato para manejar el tipo de TOUR"""
    class Meta:
        # Se relaciona con el origen de la data en models.Tour 
        model = Tour 


class SalidaType(DjangoObjectType): 
    """ Tipo de dato para manejar el tipo de SALIDA"""
    class Meta:
        #Se RELACIONA con el origen de la data en models.Salida
        
        model = Salida


class Query(graphene.ObjectType):  # ver video: 03:23:03

    """ Definición de las "respuestas" a las consultas posibles """

    # Se definen los posibles CAMPOS DE LAS CONSULTAS

    all_users = graphene.List(UserType) #allUsers
    all_zonas = graphene.List(ZonaType) #allZonas
    all_tours = graphene.List(TourType) #allTours
    all_salidas = graphene.List(SalidaType) #allSalidas

    # Se define las respuestas para cada campo definido

    def resolve_all_users(self, info, **kwargs):
        # Responde con la lista de todos registros 

        return User.objects.all()

    def resolve_all_zonas(self, info, **kwargs):
        # Responde con la lista de todos registros 

        return Zona.objects.all()

    def resolve_all_tours(self, info, **kwargs):

        return Tour.objects.all()

    def resolve_all_salidas(self, info, **kwargs):

        return Salida.objects.all()


class CreateZona(graphene.Mutation):

    """Permite realizar la operación de crear en la tabla "Zona"""

    class Arguments:
        """ Define los argumentos para crear una Zona"""

        nombre = graphene.String(required=True)
        descripcion = graphene.String()
        latitud = graphene.Decimal()
        longitud = graphene.Decimal()

    #El atributo usado para la respuesta de la mutación

    zona = graphene.Field(ZonaType)

    def mutate(self, info, nombre, descripcion=None, latitud=None, longitud=None):


        """Se encarga de crear la nueva Zona donde solo NOMBRE es obligatorio, el resto de los atributos son opcionales"""

        zona = Zona(
            nombre=nombre,
            descripcion=descripcion,
            latitud=latitud,
            longitud=longitud
        )
        zona.save()

        # Se regresa una instancia de esta mutación y como parámetro la Zona creada

        return CreateZona(zona=zona)

class Mutation(graphene.ObjectType):
    create_zona = CreateZona.Field()

# schema = graphene.Schema(query=Query)

schema = graphene.Schema(query=Query, mutation=Mutation)

