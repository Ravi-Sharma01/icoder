from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    post = Post.objects.filter().last()
    context = {'post': post}
    return render(request, 'home/home.html', context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request, 'Please fill the form correctly!')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been sent successfully.')
        

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>78 or len(query)<1:
        allPosts = Post.objects.none() # blank query
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)

    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {'allposts': allPosts, 'query':query}
    return render(request, 'home/search.html', params)

def handleSignUp(requst):
    if requst.method=='POST':
        # get the post parameters
        username = requst.POST['username']
        email = requst.POST['email']
        fname = requst.POST['fname']
        lname = requst.POST['lname']
        pass1 = requst.POST['pass1']
        pass2 = requst.POST['pass2']
        print("hello", username,  fname, lname, email, pass1)
        # check for errorneous input
        if len(username)>10:
            messages.warning(requst, 'Your username must be under 10 charachter.' )
            return redirect('home')
        if not username.isalnum():
            messages.warning(requst, 'Username should only contain letters and numbers.')
            return redirect('home')
        if pass1 != pass2:
            messages.warning(requst, 'Passswords do not match.')
            return redirect('home')

        # create the user
        myuser = User.objects.create_user(username, email, pass1) 
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(requst, "Your icoder has been submitted successfully!")       
        return redirect('home')
    else:
        return HttpResponse('404- notfound')
    
def handleLogIn(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginuserpassword = request.POST['loginuserpassword']

        user = authenticate(username=loginusername, password=loginuserpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect('home')
        
        else:
            messages.error(request, 'invalid credentials! please try again')
            return redirect('home')
    else:
        return HttpResponse('404- not found')


def handleLogOut(request):
    logout(request)
    messages.success(request, 'successfully logged out')
    return redirect('home')