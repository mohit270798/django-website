from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    logo = models.CharField(max_length=50)

    def __str__(self):
        return self.title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    file_type = models.CharField(max_length=5)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title) + ' - ' + str(self.file_type)
