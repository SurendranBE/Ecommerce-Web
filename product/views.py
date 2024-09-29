from django.shortcuts import render, get_object_or_404, redirect
from product.forms import ProductForm
from product.models import Product
from category.models import Category
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

def add_product(request):
    if request.session.has_key('user_id'):
        username = request.session['username'].capitalize()
        categories = Category.objects.all()
        return render(request, 'eadmin/product.html', {'username': username,'categories':categories})
    
    else:
        return redirect('/eadmin')
    
def ajax_insert(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'save_status': 'Success'})
        else:
            return JsonResponse({'save_status': 'Failed', 'errors': form.errors})
    return JsonResponse({'save_status': 'Invalid request'})

def product_view(request):
    product_list = Product.objects.all()
    return render(request, 'eadmin/view_product.html', {'product_list': product_list})


def product_edit(request, id):
        product_edit = Product.objects.get(id=id)
        return render(request, 'eadmin/edit_product.html', {'product_edit': product_edit})

def ajax_edit(request, id):
    data = ""
    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        if request.FILES:
            form = ProductForm(request.POST, files=request.FILES, instance=product)
        else:
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            data = json.dumps({'update_status': "Success"})
        else:
            data = json.dumps({'update_status': "Failed"})
    
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def active_product(request, id):
    if request.method == 'POST':
        available = request.POST.get('available', None)
        active_update = Product.objects.filter(id=id).update(Available=available)
        if active_update:
            return JsonResponse({'update_status': "Success"})
        return JsonResponse({'update_status': "Failed"})
    return JsonResponse({'update_status': "Invalid request"})

@csrf_exempt
def available_product(request, id):
    if request.method == 'POST':
        available_update = Product.objects.filter(id=id).update(draft_available=1)
        if available_update:
            return JsonResponse({'update_status': "Success"})
        return JsonResponse({'update_status': "Failed"})
    return JsonResponse({'update_status': "Invalid request"})


def remove_image(request, id):
    data = ""
    image_type = request.POST.get('image_type', None)
    if image_type == "image":
        image_update =Product.objects.get(id=id)
        try:
            image_update.delete_image('image')
        except:
            data = json.dumps({'update_status': "Success"})
    return HttpResponse(data, content_type='application/json')
