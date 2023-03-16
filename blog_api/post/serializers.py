from rest_framework import serializers
from .models import Category, Tag, Post, Comment, Rating
from django.db.models import Avg


class CategorySerializer(
    serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title',) # выводим только тайтл, так ака слаг это юрай


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('title',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.name') # мы не хотим чтобы поле заполнялось поле только для чтения

    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, title): # валидация на уникайльный тайлт( чтобы название не повторядось)
        if self.Meta.model.objects.filter(
                title=title).exists(): # exists проверяет на булевое знаяение нашего тайлта - совпадает или нет
            raise serializers.ValidationError(
                'Такой заголовок уже существует'
            )
        return title

    def create(self, validated_data):
        request = self.context.get('request') # получаем контекст с реквеста
        user = request.user # юзер который отпрправил запрос
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(author=user,
                        **validated_data)
        post.tags.add(*tags)
        return post

    def to_representation(self, instance): # для вывода даных (для презентаци данныз)
        representation = super().to_representation(instance) # в инстанс прилетает объект, для какого объекта отобрахить (объект для которого мы отобараем эти данные в гет запросе0)
        representation['comments'] = CommentSerializer(Comment.objects.filter(post=instance.pk),many=True).data
        # representation['ratings'] = RatingSerializer(Rating.objects.filter(post=instance.pk), many=True).data
        representation['ratings'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        representation['likes_count'] = instance.likes.count()
        return representation


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'slug',
                  'image', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.name')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Comment.objects.create(author=user,
                        **validated_data)
        return comment

    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Rating
        fields = ['id', 'rating', 'author', 'post']

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating')
        instance.save()
        return super().update(instance, validated_data)

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError('Рейтинг должен быть от 1 до 5')
        return rating

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Rating.objects.create(author=user,
                        **validated_data)
        return comment
        