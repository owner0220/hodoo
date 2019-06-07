from django.db import models
from django.conf import settings

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=30)
    poster_path = models.CharField(max_length=140)
    poster_back = models.CharField(max_length=140)
    overview = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movie_set",blank=True)
    watch = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="watched",blank=True)
    def __str__(self):
        return self.title


class Score(models.Model):
    content =  models.CharField(max_length=140)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    current_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)