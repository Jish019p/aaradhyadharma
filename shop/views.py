from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders
from django.template import loader


def index(request):
    return render(request,"shop/index.html")
def about(request):
    return render(request,"shop/about.html")
# def contact(request):
#     return render(request,"shop/contact.html")
def tracker(request):
    return render(request,"shop/index.html")
def search(request):
    return render(request,"shop/index.html")
def products(request):
    return render(request,"shop/index.html")
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        # update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        # update.save()
        # thank = True
        # id = order.order_id
    return render(request,"shop/checkout.html")
def handlerequest(request):
    return render(request,"shop/index.html")
# Create your views here.
def product(request):
    product=Product.objects.all().values( )
    template=loader.get_template('shop/index.html')
    context={
        'product':product,
             }
    return HttpResponse(template.render(context,request))

def viewp(request,id):
    product=Product.objects.get(id=id)
    template=loader.get_template('shop/product.html')
    context={
        'Product':product,
             }
    return HttpResponse(template.render(context,request))

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'shop/contact.html', {'thank': thank})