from django.shortcuts import render, HttpResponse
from blog.models import Post

# Create your views here.

def blogHome(request):
    allposts = Post.objects.all()
    context = {'allposts': allposts}
    return render(request, 'blog/blogHome.html', context)
#   return HttpResponse("this is bloghome. we will keep all the blogposts here")

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'blog/blogPost.html', context=context)
#   return HttpResponse(f"this is blopost.{slug} ")