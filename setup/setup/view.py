from django.db import models
from django.shortcuts import render, redirect


def product(request):
  product_name = request.Post.get('name',"")
  product_desc = request.Post.get('desc',"")
  product_price= request.Post.get('price',"")
  product_size= request.Post.get('size',"")
  product_quality = request.Post.get('quality',"")

def productColour(request):
  products = Product.objects.all()
  return (request,  {'products': products})

def productImage(request):
    if request.method == 'POST':
      form = UserImageForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        img_object = form.instance

        return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})
    else:
      form = UserImageForm()

    return render(request, 'image_form.html', {'form': form})


def __str__(self):
  return self.title