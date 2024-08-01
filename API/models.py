from django.db import models
from .helpers import SaveMedia


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class Albom(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
