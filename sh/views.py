from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

class Product:
    def __init__(self, name, price ):
        self.name = name
        self.price = int(price)


        if self.price >= 100:
            self.typ = True
        else:
            self.typ = False


prodects=[]

class productForm(forms.Form):
    name = forms.CharField(label='name')
    price = forms.IntegerField(label ='price')

def index(request):
    total=0

    for prodect in prodects:
        total += prodect.price

    return render(request, 'sh/index.html',{'prodects':prodects,'total':total})

def add(request):
  if request.method == "POST":
      form = productForm(request.POST)
      if form.is_valid():
        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        product = Product(name, price)
        prodects.append(product)

        return HttpResponseRedirect(reverse('sh:index'))
  else:
     form = productForm()
  return render(request, 'sh/add.html',{'form':form})
def expenses(request):
    expensive_products = []

    for prodect in prodects:
        if prodect.typ == True:
            expensive_products.append(prodect)

    return render(request, 'sh/expensive.html',
                  {'expensive': expensive_products})
# Create your views here.
