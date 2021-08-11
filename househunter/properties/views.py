from django.shortcuts import render, redirect
from .models import Location, Property
# Create your views here.

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

def viewProperty(request, pk):
    property = Property.objects.get(id=pk)
    return render(request, 'properties/property.html', {'property': property})

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


