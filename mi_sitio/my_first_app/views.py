from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

def my_view(request):
    car_list = [
        {"title": "Ford Ranger"},
        {"title": "Chevrolet S10"},
        {"title": "Toyota Hilux"},
    ]

    context = { 
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)

class CarListView(TemplateView):
    template_name = "my_first_app/car_list.html"

    def get_context_data(self):
        car_list = [
            {"title": "Ford Ranger"},
            {"title": "Chevrolet S10"},
            {"title": "Toyota Hilux"},
        ]
        return {
            "car_list": car_list
        }

def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")
