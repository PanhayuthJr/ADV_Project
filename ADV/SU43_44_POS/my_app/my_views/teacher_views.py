from itertools import product

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from unicodedata import category

from my_app.models import Category, Student, Teacher


# Create your views here.

def index(request):
    search_query = request.GET.get('search_item', '')  # get search query from GET parameter

    if search_query:
        # filter by first_name or last_name
        teachers = Teacher.objects.filter(first_name__icontains=search_query) | \
                   Teacher.objects.filter(last_name__icontains=search_query)
    else:
        teachers = Teacher.objects.all()

    paginator = Paginator(teachers, 5)  # paginate 5 per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {
        "teachers": page_obj,
        "count_items": teachers.count(),
        "search_query": search_query,  # pass current search term for template
    }
    return render(request, "pages/Teacher/index.html", context=data)
def show(request):
    return render(request, "pages/Teacher/create.html")
def create(request):
    if request.method == 'POST':
        teacher = Teacher()
        teacher.first_name = request.POST['first_name']
        teacher.last_name = request.POST['last_name']
        teacher.gender = request.POST['gender']
        teacher.address = request.POST['address']
        teacher.dob = request.POST['dob']
        teacher.salary = request.POST['salary']
        teacher.full_clean()
        teacher.save()
        messages.success(request, "Teacher created successfully")
        return redirect('Teacher_show')
    return render(request, 'pages/Teacher/create.html')

def delete_by_id(request,id):
    teacher = Teacher.objects.get(pk=id)
    teacher.delete()
    messages.success(request, "Teacher deleted successfully")
    return redirect('teacher_index')
def edit_by_id(request, id):
    teacher = Teacher.objects.get(pk=id)
    data = {"teacher": teacher}  # lowercase and singular
    return render(request, "pages/Teacher/edit.html", context=data)
def update_by_id(request, id):
    teacher_existing = Teacher.objects.get(pk=id)
    teacher_existing.first_name = request.POST['first_name']
    teacher_existing.last_name = request.POST['last_name']
    teacher_existing.gender = request.POST['gender']
    teacher_existing.address = request.POST['address']
    teacher_existing.dob = request.POST['dob']
    teacher_existing.salary = request.POST['salary']
    teacher_existing.full_clean()
    teacher_existing.save()
    messages.success(request, "Teacher updated successfully")
    return redirect(f"/teacher/edit_by_id/{id}")