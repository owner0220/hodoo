from django.contrib.auth import get_user_model
from Movies.models import Movie
from rest_framework import viewsets
from .serializers import UserSerializer, MovieSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer