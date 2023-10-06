from django.urls import path

# from django.views.decorators.csrf import csrf_exempt
from graphql_jwt.decorators import jwt_cookie
from graphene_django.views import GraphQLView

# from . import schema

urlpatterns = [
    path("", jwt_cookie(GraphQLView.as_view(graphiql=True))),
]
