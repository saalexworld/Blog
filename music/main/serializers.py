from rest_framework import serializers
from .models import Album, Song


class AlbumSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    artist = serializers.CharField(required=True)

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            'title', instance.title)
        instance.artist = validated_data.get(
            'artist', instance.artist
        )
        return instance


class SongSerializer(serializers.Serializer):
    title = serializers.CharField(
        required=True)
    order = serializers.IntegerField()
    duration = serializers.IntegerField()
    album = serializers.SlugRelatedField(
        queryset=Album.objects.all(),
        slug_field='title'
    )
    # album = serializers.PrimaryKeyRelatedField(
    #     queryset=Album.objects.all())

    def create(self, validated_data):
        return Song.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get(
            'title', instance.title)
        instance.order = validated_data.get(
            'order', instance.order
        )
        instance.duration = validated_data.get(
            'duration', instance.duration
        )
        instance.album = validated_data.get(
            'album', instance.album
        )
        return instance

