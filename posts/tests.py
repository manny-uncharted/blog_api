from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# Create your tests here

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        # Create a user
        testuser1 = User.objects.create_user(
            username = 'testuser1', password='abc123'
        )
        testuser1.save()

        # create blog post

        test_post = Post.objects.create(
            author = testuser1, title = 'A blog post', body='Body Content ...'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'A blog post')
        self.assertEqual(body, 'Body Content ...')