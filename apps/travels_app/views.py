from django.shortcuts import render, redirect
from .models import Trip, User
from django.contrib import messages

# Create your views here.
def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

def checkUser(request):
	try:
		if request.session['f_name'] < 3:
			return False
		else:
			return True
	except:
		return False

def home(request):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    context = {
        'myTrips': Trip.objects.filter(planned_by=User.objects.get(id=request.session['user_id'])),
        'joinedTrips': Trip.objects.filter(users_joined=User.objects.get(id=request.session['user_id'])),
        'others': Trip.objects.all().exclude(planned_by=User.objects.get(id=request.session['user_id'])).exclude(users_joined=User.objects.get(id=request.session['user_id'])),
    }
    print context['joinedTrips']
    return render(request, 'travels_app/index.html', context)

def add(request):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    return render(request, 'travels_app/add.html')

def addTrip(request):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    results = Trip.objects.tripVal(request.POST)
    if results['status'] == True:
        Trip.objects.createTrip(request.POST)
    else:
        genErrors(request, results['errors'])
        return redirect('/travels/add')
    return redirect('/travels')

def destination(request, id):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    context = {
        "trip": Trip.objects.get(id=id),
        "others": User.objects.filter(joined_users__in=Trip.objects.filter(id=id))
    }

    return render(request, 'travels_app/destination.html', context)

def join(request, id):
    results = checkUser(request)
    if results == False:
        return redirect('/')
    trip = Trip.objects.get(id=id)
    trip.users_joined.add(User.objects.get(id=request.session['user_id']))
    return redirect('/travels')
