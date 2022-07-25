from django.shortcuts import redirect, render
from .models import Product, Order
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    if request.method == 'POST':
        id= request.POST.get('productid')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(id)
            if quantity:
                cart[id]=quantity+1
            else:
                cart[id]=1
        else:
            cart={}
            cart[id]=1
        request.session['cart']=cart
        print(request.session['cart'])
    product_obj = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_obj = product_obj.filter(title__icontains=item_name)

    paginator = Paginator(product_obj, 8)
    page = request.GET.get('page')
    product_obj = paginator.get_page(page)

    le=0
    if request.session.get('cart') is not None:
        ids= list(request.session.get('cart').keys())
        quan=list(request.session.get('cart').values())
    
        items = Product.objects.filter(id__in=ids)
    
    
        l=[]
        s=int()
        for i,q in zip(items,quan):
        
            l.append(i.price*q)
            s=s+(i.price*q)

    
        flist=list(zip(items,quan,l))
        le=len(flist)
   

    
    

    return render(request, 'shop/index.html', {'product_obj': product_obj,'le':le})


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
        order = Order(items=items, name=name, email=email, address=address,
        city=city, state=state, zipcode=zipcode, total=total)
        order.save()
        del request.session['cart']
        return redirect('/')
    
        
    ids= list(request.session.get('cart').keys())
    quan=list(request.session.get('cart').values())
    
    items = Product.objects.filter(id__in=ids)
    
    
    l=[]
    s=int()
    for i,q in zip(items,quan):
        
        l.append(i.price*q)
        s=s+(i.price*q)

    print(l)
    flist=list(zip(items,quan,l))
    le=len(flist)
    
    return render(request, 'shop/checkout.html',{'s':s,'flist':flist})
