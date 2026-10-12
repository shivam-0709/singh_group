from django.shortcuts import render

items = [
    {"name": "Shoes", "price": "1200", "desc": "Comfortable running shoes", "image": "images/shoes.jpg"},
    {"name": "Watch", "price": "2500", "desc": "Stylish wrist watch", "image": "images/watch.jpg"},
    {"name": "Shirt", "price": "1100", "desc": "Comfortable cool shirt", "image": "images/formal-shirt.jpg"},
    {"name": "T-Shirt", "price": "400", "desc": "Funky T-shirt", "image": "images/T-shirt.jpg"},
    {"name": "Jacket", "price": "6000", "desc": "Classy Jacket", "image": "images/jacket.jpg"},
    {"name": "Jeans", "price": "1800", "desc": "Jeans with Style", "image": "images/jeans.jpg"},
]

def index(request):
    return render(request, "index.html", {"items": items})
