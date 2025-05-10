from django.shortcuts import render
from .models import Bus, Train
from django.http import JsonResponse

def suggest_routes(request):
    query = request.GET.get('term', '')
    buses = Bus.objects.all()
    trains = Train.objects.all()
    suggestions = set()

    for bus in buses:
        suggestions.add(bus.start_point.strip())
        suggestions.add(bus.destination_point.strip())
        suggestions.update(via.strip() for via in bus.via.split(','))
    for train in trains:
        suggestions.add(train.start_point.strip())
        suggestions.add(train.destination_point.strip())
        suggestions.update(via.strip() for via in train.via.split(','))

    results = [s for s in suggestions if query.lower() in s.lower()]
    return JsonResponse(results, safe=False)

def home(request):
    return render(request, 'timetable/home.html')

from django.db.models import Q

def filter_routes(model, start, destination):
    if start and destination:
        return model.objects.filter(
            Q(start_point__icontains=start) | Q(via__icontains=start) | Q(destination_point__icontains=start),
            Q(start_point__icontains=destination) | Q(via__icontains=destination) | Q(destination_point__icontains=destination)
        )
    elif start:
        return model.objects.filter(
            Q(start_point__icontains=start) | Q(via__icontains=start) | Q(destination_point__icontains=start)
        )
    elif destination:
        return model.objects.filter(
            Q(start_point__icontains=destination) | Q(via__icontains=destination) | Q(destination_point__icontains=destination)
        )
    return model.objects.all()


def search_buses(request):
    start = request.GET.get('start', '')
    destination = request.GET.get('destination', '')
    buses = filter_routes(Bus, start, destination)

    for bus in buses:
        bus.via_list = [v.strip() for v in bus.via.split(',')]
    
    return render(request, 'timetable/bus_results.html', {'buses': buses})

def search_trains(request):
    start = request.GET.get('start', '')
    destination = request.GET.get('destination', '')
    trains = filter_routes(Train, start, destination)

    for train in trains:
        train.via_list = [v.strip() for v in train.via.split(',')]
    
    return render(request, 'timetable/train_results.html', {'trains': trains})
