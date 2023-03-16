# from django.test import TestCase

# Create your tests here.


from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.core.files import File
from .views import PostViewSet
from .models import Post, Category
from account.models import User
from collections import OrderedDict


class PostTest(APITestCase):
    def setUp(self) -> None: # отрабатывает всегда - вснегда пишется во всех тестах
        self.factory = APIRequestFactory()
        self.category = Category.objects.create(
            title = 'cat1',
        )
        user = User.objects.create_user(
            email='test@gmail.com', 
            password='1234',
            is_active=True,
            name='Test',
            last_name='User'
        )
        img = File(open('posts/Снимок_экрана_2023-01-10_в_23.36.15_ACMeNNn.png', 'rb'))
        posts = [
            Post(author=user, body='new post', title='post1', image=img, category=self.category, slug='1'),
            Post(author=user, body='new post2', title='post1', image=img, category=self.category, slug='2'),
            Post(author=user, body='new post3', title='post1', image=img, category=self.category, slug='3')
        ]

        Post.objects.bulk_create(posts)
    
    def test_list(self):
        request = self.factory.get('posts/')
        view = PostViewSet.as_view({'get': 'list'})
        response = view(request)
        # print(response.data)

        self.assertEqual(response.status_code, 200)
        assert type(response.data) == OrderedDict

    def test_retrieve(self):
        slug = Post.objects.all()[0].slug
        request = self.factory.get(f'posts/{slug}/')
        view = PostViewSet.as_view({'get':'retrieve'})
        response = view(request, pk=slug)
        print(response.data)

        assert response.status_code == 200

# дома сделать апдейт и делет = test_update test_delete test_forgot_password_complete

    def test_create(self):
        user = User.objects.all()[0]
        data = {
            'body': 'sdqwdwqdw',
            'title': 'post4',
            'category': 'cat1'
        }
        request = self.factory.post(
            'posts/', data, format='json'
        )
        force_authenticate(request, user=user)
        view = PostViewSet.as_view({'post': 'create'})
        response = view(request)
        print(response.data)

        assert response.status_code == 201
        assert response.data['body'] == data['body']
        assert Post.objects.filter(
            author=user, body=data['body']
        ).exists()



