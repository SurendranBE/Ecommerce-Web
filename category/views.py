from django.shortcuts import render, get_object_or_404, redirect
from category.forms import CategoryForm, CategoryForms
from category.models import Category
import json
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def add_category(request):
    if request.session.has_key('user_id'):
        username = request.session['username'].capitalize()
        return render(request, 'eadmin/category.html', {'username': username, 'menu': 'category'})
    else:
        return redirect('/eadmin')


def ajax_insert(request):
    data = ""
    if request.method == 'POST':
        form = CategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            data = json.dumps({'save_status': "Success"})
        else:
            data = json.dumps({'save_status': "Failed"})
    return HttpResponse(data, content_type='application/json')

def category_view(request):
        category_list = Category.objects.all()
        return render(request, 'eadmin/view_category.html', {'category_list': category_list})

def category_edit(request, id):
        category_edit = Category.objects.get(id=id)
        return render(request, 'eadmin/edit_category.html', {'category_edit': category_edit})

def ajax_edit(request, id):
    data = ""
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        if request.FILES:
            form = CategoryForm(request.POST, files=request.FILES, instance=category)
        else:
            form = CategoryForms(request.POST, instance=category)
        if form.is_valid():
            form.save()
            data = json.dumps({'update_status': "Success"})
    return HttpResponse(data, content_type='application/json')

def active_category(request, id):
    data = ""
    status = request.GET.get('status', None)
    active_update = Category.objects.filter(id=id).update(visibility=status)
    if active_update:
        data = json.dumps({'update_status': "Success"})
    return HttpResponse(data, content_type='application/json')

def publish_category(request, id):
    data = ""
    publish_update = Category.objects.filter(id=id).update(draft_status=1)
    if publish_update:
        data = json.dumps({'update_status': "Success"})
    return HttpResponse(data, content_type='application/json')

def remove_image(request, id):
    data = ""
    image_type = request.POST.get('image_type', None)
    if image_type == "image":
        image_update = Category.objects.get(id=id)
        try:
            image_update.delete_image('image')
        except:
            data = json.dumps({'update_status': "Success"})
    if image_type == "banner":
        banner_update = Category.objects.get(id=id)
        try:
            banner_update.delete_banner('banner_img')
        except:
            data = json.dumps({'update_status': "Success"})
    return HttpResponse(data, content_type='application/json')














