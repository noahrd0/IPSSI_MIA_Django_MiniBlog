from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_blog_posts, name='list_blog_posts'),
    path('post/<int:post_id>/', views.view_blog_post, name='view_blog_post'),
    path('post/<int:post_id>/delete/', views.delete_blog_post, name='delete_blog_post'),
    path('post/<int:post_id>/edit/', views.edit_blog_post, name='edit_blog_post'),
    path('post/create/', views.create_blog_post, name='create_blog_post'),

    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<int:post_id>/add_comment/', views.create_comment, name='create_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
]
