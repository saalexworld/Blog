from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Category, Tag, Post, \
    Comment, Like, Rating
from .permission import IsAdminAuthPermission,\
    IsAuthorPermission
from .serializers import CategorySerializer, \
    TagSerializer, PostSerializer, PostListSerializer,\
    CommentSerializer, RatingSerializer
import django_filters #pip install django-filter
from rest_framework import filters
from rest_framework.decorators import action


class CategoryListView( #есть нам нет необходимсоти реалтзовывать весь крад
    generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# class PostListCreateView(
#     generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['category']
#     search_fields = ['tags__slug', 'created_at']
#
# class PostDetailView(
#     generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['tags__slug', 'created_at']
    ordering_fields = ['created_at', 'title']

    # api/v1/posts/pk(post1)/comments/
    @action(['GET'], detail=True) # он добавляет 1 действие к маршруту при определенных запросах (апивью мы прописываем туда запросы) экшен как дооплнение 
    def comments(self, request, pk=None):
        post = self.get_object()
        comments = post.comments.all()
        serializer = CommentSerializer(
            comments, many=True)
        return Response(serializer.data)

    @action(['POST', 'PATCH'], detail=True)
    def rating(self, request, pk=None):
        data = request.data.copy()
        data['post'] = pk
        serializer = RatingSerializer(
            data=data, context={'request': request}
        )
        rating = Rating.objects.filter(
            author=request.user,
            post=pk
        ).first()
        if serializer.is_valid(raise_exception=True):
            if rating and request.method == 'POST':
                return Response('use PATCH method')
            elif rating and request.method == 'PATCH':
                serializer.update(rating,
                        serializer.validated_data)
                return Response('Updated')
            elif request.method == 'POST':
                serializer.create(
                    serializer.validated_data)
                return Response('Created')

    @action(['POST'], detail=True)
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        try:
            like = Like.objects.get(
                post=post, author=user)
            like.is_liked = not like.is_liked
            like.save()
            message = 'liked' if like.is_liked else 'disliked'
            if not like.is_liked:
                like.delete()
        except Like.DoesNotExist:
            Like.objects.create(
                post=post, author=user,
                is_liked=True)
            message = 'liked'
        return Response(message, status=200)


    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'create':
            self.permission_classes = [
                IsAdminAuthPermission]
        elif self.action in ['update',
                    'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]

        return super().get_permissions()


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'create':
            self.permission_classes = [
                IsAdminAuthPermission]
        elif self.action in ['update',
                    'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]

        return super().get_permissions()