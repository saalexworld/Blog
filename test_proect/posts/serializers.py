from rest_framework import serializers
# сначала импроты встроенные, потом импроты библиотек потом папки наши
from .models import Post ,Category


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__' # могут быть проблемы, лучше каждлоре поле вызываьб по отдельности


class CategorySerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # title = serializers.CharField()

    class Meta:
        model = Category
        fields = '__all__'
