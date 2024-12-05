from django.test import TestCase, Client
from django.urls import reverse
from .models import BlogPost, Comment

class BlogPostTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog_post = BlogPost.objects.create(title="Test Post", content="Test Content")

    def test_create_blog_post(self):
        response = self.client.post(reverse('create_blog_post'), {
            'title': 'New Post',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(BlogPost.objects.filter(title='New Post').exists())

    def test_edit_blog_post(self):
        response = self.client.post(reverse('edit_blog_post', args=[self.blog_post.id]), {
            'title': 'Updated Post',
            'content': 'Updated Content'
        })
        self.assertEqual(response.status_code, 302)
        self.blog_post.refresh_from_db()
        self.assertEqual(self.blog_post.title, 'Updated Post')

    def test_delete_blog_post(self):
        response = self.client.post(reverse('delete_blog_post', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(BlogPost.objects.filter(id=self.blog_post.id).exists())

class CommentTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog_post = BlogPost.objects.create(title="Test Post", content="Test Content")
        self.comment = Comment.objects.create(blog_post=self.blog_post, author="Test Author", content="Test Comment")

    def test_create_comment(self):
        response = self.client.post(reverse('create_comment', args=[self.blog_post.id]), {
            'author': 'New Author',
            'content': 'New Comment'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(content='New Comment').exists())

    def test_edit_comment(self):
        response = self.client.post(reverse('edit_comment', args=[self.comment.id]), {
            'author': 'Updated Author',
            'content': 'Updated Comment'
        })
        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated Comment')

    def test_delete_comment(self):
        response = self.client.post(reverse('delete_comment', args=[self.comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=self.comment.id).exists())

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.blog_post = BlogPost.objects.create(title="Test Post", content="Test Content")

    def test_list_blog_posts_view(self):
        response = self.client.get(reverse('list_blog_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')
        self.assertContains(response, 'Test Post')

    def test_view_blog_post_view(self):
        response = self.client.get(reverse('view_blog_post', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, 'Test Post')

    def test_redirection_after_create_blog_post(self):
        response = self.client.post(reverse('create_blog_post'), {
            'title': 'New Post',
            'content': 'New Content'
        })
        self.assertRedirects(response, reverse('list_blog_posts'))