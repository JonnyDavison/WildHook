import unittest
from django.contrib.auth.models import User
from .models import Post
from django.core.exceptions import ObjectDoesNotExist

class PostModelTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test user if it doesn't exist
        cls.test_user, _ = User.objects.get_or_create(username='testuser_unique')

        # Create a test post with a unique title and slug
        cls.test_post = Post.objects.create(
            title='Unique Test Post 10',
            author=cls.test_user,
            description='Test Description',
            content='Test Content',
            tags='ORVIS',
            categories='NEWS',
            slug='unique-test-post10',  # Set a specific slug for testing
            meta_description='Test Meta Description',
            meta_keywords='Test Meta Keywords'
        )

    def test_post_title(self):
        self.assertEqual(self.test_post.title, 'Unique Test Post 10')

    def test_post_slug(self):
        self.assertEqual(self.test_post.slug, 'unique-test-post10')

    def test_post_absolute_url(self):
        expected_url = f'/blog/post/{self.test_post.slug}/'
        self.assertEqual(self.test_post.get_absolute_url(), expected_url)

    def tearDown(self):
        try:
            test_post = Post.objects.get(slug='unique-test-post10')
            test_post.delete()
        except ObjectDoesNotExist:
            pass

if __name__ == '__main__':
    unittest.main()