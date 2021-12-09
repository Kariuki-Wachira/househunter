from django.contrib.auth import forms
from django.shortcuts import render, redirect
from .models import Location, Property, Wishlist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate (request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        
        # forms = {
        #     errors
        # }

    return render(request,'properties/login_register.html', {'page': page,})

def logoutUser(request):
    logout(request)
    return redirect('homepage')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate (request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('homepage')

    print(form)
    context = {'form': form, 'page': page}
    return render(request, 'properties/login_register.html', context)

def homepage(request):
    location = request.GET.get('location')
    username=request.user.get_username()

    if location == None:
        properties = Property.objects.all()
    else:
        properties = Property.objects.filter(location__name =location)

    locations = Location.objects.all()

    context = {'locations': locations, 'properties': properties, 'username': username}
    return render(request, 'properties/homepage.html', context)

def staffrequest(request):
    username=request.user.get_username()
    user = request.user
    context = {'username': username}
    return render(request, 'properties/staffreq.html', context)


def viewProperty(request, pk):
    property = Property.objects.get(id=pk)
    return render(request, 'properties/property.html', {'property': property})

# @login_required(login_url='login')
def viewmywishlist(request):
    user = request.user
    wishes = Wishlist.objects.filter(user=user)

    context = {'wishes': wishes}
    return render(request, 'properties/wishlist.html', context)

@login_required(login_url='login')
def addToWishlist(request,pk):
    user = request.user
    property = Property.objects.get(id=pk)
    Wishlist.objects.create(user=user,property=property)

    return redirect('property',pk=pk)


@login_required(login_url='login')
@staff_member_required(login_url='staffrequest')
def addProperty(request):
    locations = Location.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['location'] !='none':
            location = Location.objects.get(id=data['location'])
        elif data ['location_new'] != '':
            location, created = Location.objects.get_or_create(name=data['location_new'])
        else:
            location = None

        property = Property.objects.create(
            image = image,
            location =location,
            description=data['description'],
            availabilitystatus=data['availabilitystatus'],
            price=data['price'],
            contacts=data['contacts'],
        )

        return redirect('homepage')

    context = {'locations': locations}
    return render(request, 'properties/add.html', context)


