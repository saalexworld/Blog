from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album,
                    on_delete=models.CASCADE,
                    related_name='songs')
    duration = models.IntegerField()
    order = models.IntegerField()
