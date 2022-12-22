from queue import Empty
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Like, Category
# Create your views here.


#New Image upload
@login_required(login_url = "auth")
def add(request):
  context = {}
  if request.method == "POST":
    title = request.POST.get("title")
    description = request.POST.get("description")
    category = request.POST.get("category")
    post_image = request.FILES.get("image")
    
    user = request.user;
    
    cat_array = Category.objects.filter(category_name = category)
    if not(cat_array.count() > 0):
      cat = Category(category_name = category)
      cat.save()
    else:
      cat = Category.objects.get(category_name = category)   
    
    profile = Profile.objects.get(user = user)
    like = Like(like_no = 0, view_no = 0)
    like.save()
    Post.objects.create(title = title, description = description,
                post_image = post_image, category = cat, 
                user = user, profile = profile, like = like)
  
    return redirect('home')        
         
  return render(request, "PhotoApp/add.html", context)

home_context = {}

@login_required(login_url = "auth")
def home(request):
  # context = {}
  search_name = ""
  Profile.objects.get_or_create(user = request.user)
  if request.method == "POST":
    profile =  Profile.objects.get(user = request.user)    
    image = request.FILES.get("change-profile")
    profile.image = image
    profile.save()
    home_context = {"image_url": profile.image}
    
    
  else:
    profile =  Profile.objects.get(user = request.user)
    home_context = {"image_url": profile.image}
    search_name = request.GET.get('name')
    
  #PERSONAL_POSTS
  user = request.user
  profile = Profile.objects.get(user = request.user)
  home_context["posts"] = user.post_set.all()
  home_context["likes"] = Like.objects.filter()
  home_context["profile_image"] = profile.image
  

  #ALL_POSTS
  if(search_name != ""):
    if(search_name != "all"):
      cat = Category.objects.filter(category_name = search_name).first()
      if cat is not None:
        cat_post = cat.post_set.all()
        home_context["all_posts"] = cat_post
        
      else:        
        all_posts = Post.objects.all() 
        home_context["all_posts"] = all_posts  
    else:
      all_posts = Post.objects.all() 
      home_context["all_posts"] = all_posts  
  else:
    all_posts = Post.objects.all() 
    home_context["all_posts"] = all_posts 
  
  return render(request, "PhotoApp/home.html",home_context)

def details(request, pk):
  return HttpResponse("Detail Page")

def auth(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:    
    context = {}
    if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username = username,password =  password)
      if user is not None:
        login(request, user)
        return redirect('home')
      else:
        messages.info(request, "Wrong username or password")
       
    return render(request, "PhotoApp/auth.html", context)

def signup(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:    
    form = SignUpForm(request.POST or None)
    context = {'form':form}
    if request.method == "POST": 
      if form.is_valid():  
        form.save()
        return redirect('auth')
    
    return render(request,"PhotoApp/signup.html", context )

@login_required(login_url = "auth")
def logoutUser(request):
  print("logout is called")
  logout(request)
  return redirect('auth')
