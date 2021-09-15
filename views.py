from django.shortcuts import render,redirect
from .models import BlogPost,BlogText
from .forms import BlogTextForm
def home(request):
    return render(request,'blog/home.html')
  
# the views for the topic
def blog_post(request):
    blog_posts = BlogPost.objects.order_by('date')
    context = {'blog_posts' : blog_posts}
    return render(request,'blog/blog_post.html',context)
  
# to get the post that corresponding with the topic
def blog_text(request, blog_posts_id):
    blog_post = BlogPost.objects.get(id=blog_posts_id)
    blog_entries = blog_post.blogtext_set.order_by('date')
    context = {'blog_post':blog_post, 'blog_entries': blog_entries}
    return render(request,'blog/blog_text.html', context)
  
# to add a new post
def new_blog(request, blog_posts_id):
    # blog_entries = blog_post.blogtext_set.order_by('date')
    blog_post = BlogPost.objects.get(id=blog_posts_id)
    if request.method == 'POST':
        form = BlogTextForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.blog_post = blog_post
            new_blog.save()
            return redirect('blog:blog_text', blog_posts_id=blog_posts_id)
    else:
        form = BlogTextForm()
    context = {'form':form,'blog_post':blog_post}
    return render(request, 'blog/new_blog.html',context)
