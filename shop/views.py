from django.shortcuts import render

items = [
    {"name": "Shoes", "price": "1200", "desc": "Comfortable running shoes", "image": "images/shoes.jpg"},
    {"name": "Watch", "price": "2500", "desc": "Stylish wrist watch", "image": "images/watch.jpg"},
]

def index(request):
    return render(request, "index.html", {"items": items})
