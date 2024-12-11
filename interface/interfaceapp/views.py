from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout as auth_logout
from django.http import HttpResponseRedirect
from .forms import ShopForm
from .models import Shop,Review
from django.db import models
from django.urls import reverse
from django.db.models import Avg
from .forms import ComplaintsForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'registration.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('add_shop')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout(request):
    auth_logout(request)  # Logs out the user
    return redirect('shop_list') 

@login_required
def add_shop(request):
    #if request.user.is_authenticated():
        if request.method == 'POST':
            form = ShopForm(request.POST,request.FILES)
            if form.is_valid():
                shop = form.save(commit = False)
                shop.user = request.user
                shop.save()
                return redirect('shop_list')
        else:
            form = ShopForm()
        return render(request, 'add_shop.html', {'form': form})
    #else:
         #return redirect('login')  # Redirect to login if not authenticated
    
def shop_list(request):
    shops = Shop.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        shops = shops.filter(shop_name__icontains=search_query)  # Simple search by name
    return render(request, 'shop_list.html', {'shops': shops})

def shop_search(request):
    shops = Shop.objects.all()
    category_filter = request.GET.get('category', '')
    #location_filter = request.GET.get('location', '')
    
    if category_filter:
        shops = shops.filter(category=category_filter)
    
    #if location_filter:
        # For simplicity, assuming location is a city name (implement actual location-based filtering as needed)
        #shops = shops.filter(address__icontains=location_filter)
    
    return render(request, 'shop_search.html', {'shops': shops})

def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    # Calculate the average rating
    reviews = shop.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] if reviews.exists() else 0
    
    return render(request, 'shop_details.html', {'shop': shop, 'avg_rating': avg_rating, 'reviews': reviews})

def submit_review(request,shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        review = Review.objects.create(shop=shop, user=request.user, rating=rating, review_text=review_text)
        return HttpResponseRedirect(reverse('shop_detail', args=[shop_id]))
    return render(request, 'submit_review.html', {'shop': shop})
    

def index(request):
    return render(request,'index.html')
    

def Cantact_User(request):
    if request.method == 'POST':
        form = ComplaintsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succuess')
    else:
        form = ComplaintsForm()
    return render(request,"cantact.html",{'form':form})

def succuess(request):
    return render(request,"succuess.html")

    