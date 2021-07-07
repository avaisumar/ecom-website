from django.shortcuts import render
from .models import Product, Order
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    product_obj = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_obj = product_obj.filter(title__icontains=item_name)

    paginator = Paginator(product_obj, 4)
    page = request.GET.get('page')
    product_obj = paginator.get_page(page)

    return render(request, 'shop/index.html', {'product_obj': product_obj})


def detail(request, id):
    product_ob = Product.objects.get(id=id)
    return render(request, 'shop/detail.html', {'product_ob': product_ob})


def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total= request.POST.get('total',"")
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()
    return render(request, 'shop/checkout.html')
