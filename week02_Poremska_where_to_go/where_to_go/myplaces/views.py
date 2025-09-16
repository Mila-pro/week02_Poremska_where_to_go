from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
import random


def home(request):
    places = Place.objects.all()
    chosen = None
    if request.method == "POST" and places.exists():
        weights = [p.rating for p in places]
        chosen = random.choices(places, weights=weights, k=1)[0]
    return render(request, "myplaces/home.html", {"chosen": chosen})


def places_list(request):
    places = Place.objects.all().order_by("-created")
    return render(request, "myplaces/places_list.html", {"places": places})


def add_place(request):
    if request.method == "POST":
        title = request.POST.get("title")
        location = request.POST.get("location")
        comment = request.POST.get("comment")
        rating = request.POST.get("rating")

        try:
            rating = float(rating)
        except (TypeError, ValueError):
            rating = None

        if title and rating and 1.0 <= rating <= 5.0 and (rating * 2).is_integer():
            Place.objects.create(
                title=title,
                location=location,
                comment=comment,
                rating=rating,
            )
            return redirect("myplaces:places_list")
        else:

            return render(request, "myplaces/add_place.html", {
                "error": "Рейтинг має бути від 1 до 5 з кроком 0.5!"
            })

    return render(request, "myplaces/add_place.html")


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    return render(request, "myplaces/place_detail.html", {"place": place})