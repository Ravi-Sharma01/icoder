from django.shortcuts import render, HttpResponse

# Create your views here.

def blogHome(request):
    return render(request, 'blog/blogHome.html')
#    return HttpResponse("this is bloghome. we will keep all the blogposts here")

def blogPost(request, slug):
    return HttpResponse(f"this is blopost.{slug} ")