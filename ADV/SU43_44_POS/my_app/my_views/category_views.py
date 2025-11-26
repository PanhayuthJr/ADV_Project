from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from unicodedata import category

from my_app.models import Category

# Create your views here.

def index(request):
    if request.method == "POST":
        category = Category()
        category.category_name = request.POST['search_item']
        categories = Category.objects.filter(name=category.category_name)
        paginator = Paginator(categories, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {"categories": page_obj, "count_items": (categories.count())}
    else:
        categories = Category.objects.all()
        paginator = Paginator(categories, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {"categories": page_obj, "count_items": (categories.count())}

    return render(request, "pages/categories/index.html", context=data)
def show(request):
    return render(request, "pages/categories/create.html")
def create(request):
    if request.method == 'POST':
        category = Category()
        category.name = request.POST['name']
        category.clean()
        category.save()
        if category.pk:
            messages.success(request, "Category created successfully")
        return redirect('category_show')
    else:
        return render(request, 'pages/categories/create.html')
def delete_by_id(request,id):
    category = Category.objects.get(pk=id)
    category.delete()
    messages.success(request, "Category deleted successfully")
    return redirect('category_index')
def edit_by_id(request,id):
    category = Category.objects.get(pk=id)
    data = {"category": category}
    return render(request, "pages/categories/edit.html", context=data)
def update_by_id(request, id):
    category_existing = Category.objects.get(pk=id)
    category_existing.name = request.POST['name']
    category_existing.full_clean()
    category_existing.save()
    messages.success(request, "Category updated successfully")
    return redirect(f"/category/edit_by_id/{id}")