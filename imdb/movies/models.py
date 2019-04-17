from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Actors(models.Model):
    GENDER = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER'),
    )
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    birthdate = models.DateField(blank=False)
    sex = models.CharField(max_length=6, choices=GENDER, default='male')
    nationality = models.CharField(max_length=150, blank=False)
    is_alive = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Categories(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movies(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=False)
    release_date = models.DateField(blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actors, blank=True)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()
    author = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.text


class Awards(models.Model):
    MOIVE = 'movie'
    ACTOR = 'actor'
    KIND_CHOICES = (
        (MOIVE, "Movie"),
        (ACTOR, "Actor")
    )
    name = models.CharField(max_length=150, blank=False)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default=MOIVE)
    movie = models.ForeignKey(Movies, models.CASCADE, blank=True, null=True)
    actor = models.ForeignKey(Actors, models.CASCADE, blank=True, null=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
