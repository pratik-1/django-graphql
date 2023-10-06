import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required
from graphene_django.types import DjangoObjectType
from .models import Movie, Director
from django.shortcuts import get_object_or_404


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

    movie_age = graphene.String()

    def resolve_movie_age(self, info):
        return "Old movie" if self.year < 2000 else "New Movie"


class DirectorType(DjangoObjectType):
    class Meta:
        model = Director


class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    movies = graphene.Field(
        MovieType, id=graphene.Int(), title=graphene.String()
    )
    all_directors = graphene.List(DirectorType)

    @login_required
    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()

    def resolve_all_directors(self, info, **kwargs):
        return Director.objects.all()

    def resolve_movies(self, info, **kwargs):
        id = kwargs.get("id")
        title = kwargs.get("title")
        if id is not None:
            return Movie.objects.get(pk=id)
        if title is not None:
            return Movie.objects.get(title=title)
        return None


class MovieCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        year = graphene.Int(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, year):
        movie = Movie.objects.create(title=title, year=year)
        return MovieCreateMutation(movie=movie)


class MovieUpdateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        year = graphene.Int()
        id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, id, **kwargs):
        movie = get_object_or_404(Movie, pk=id)
        if kwargs.get("title") is not None:
            movie.title = kwargs.get("title")
        if kwargs.get("year") is not None:
            movie.year = kwargs.get("year")
        movie.save()
        return MovieUpdateMutation(movie=movie)


class MovieDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, id, **kwargs):
        movie = get_object_or_404(Movie, pk=id)
        movie.delete()
        return MovieUpdateMutation(movie=None)


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()

    create_movie = MovieCreateMutation.Field()
    update_movie = MovieUpdateMutation.Field()
    delete_movie = MovieDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
