from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class BlogTests(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Django")
        self.assertEqual(str(category), "Django")

    def test_create_post(self):
        user = User.objects.create_user(username='testuser', password='12345')
        category = Category.objects.create(name="Tech")
        post = Post.objects.create(title="Test Post", author=user, content="Test content", category=category)
        self.assertEqual(str(post), "Test Post")
