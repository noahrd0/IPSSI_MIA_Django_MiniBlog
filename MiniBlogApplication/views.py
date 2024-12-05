from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm

# ALL POSTS
def list_blog_posts(request):
    blog_posts = BlogPost.objects.all().order_by('-created_at')

    return render(request, 'post_list.html', {'blog_posts': blog_posts})

# CRUD POST
def view_blog_post(request, post_id):
    print(post_id)
    blog_post = get_object_or_404(BlogPost, id=post_id)
    comments = Comment.objects.filter(blog_post=blog_post).order_by('-created_at')
    return render(request, 'post_detail.html', {
        'blog_post': blog_post,
        'comments': comments
    })

def delete_blog_post(request, post_id):
    blog_post = BlogPost.objects.get(id=post_id)
    blog_post.delete()
    return redirect('list_blog_posts')

def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list_blog_posts')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_blog_posts')
    else:
        form = BlogPostForm()
    return render(request, 'post_form.html', {'form': form})

# CRUD COMMENT

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('view_blog_post', comment.blog_post.id)

def create_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = post
            comment.save()
            return redirect('view_blog_post', post_id)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('view_blog_post', comment.blog_post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_form.html', {'form': form})