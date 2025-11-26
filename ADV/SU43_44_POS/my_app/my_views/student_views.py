from itertools import product

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from unicodedata import category

from my_app.models import Category, Student


# Create your views here.

def index(request):
    search_query = request.GET.get('search_item', '')  # get search query from GET

    if search_query:
        students = Student.objects.filter(
            first_name__icontains=search_query
        ) | Student.objects.filter(
            last_name__icontains=search_query
        )
    else:
        students = Student.objects.all()

    paginator = Paginator(students, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {
        "students": page_obj,
        "count_items": students.count(),
        "search_query": search_query
    }

    return render(request, "pages/Student/index.html", context=data)


def show(request):
    return render(request, "pages/Student/create.html")


def create(request):
    if request.method == 'POST':
        student = Student()
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.gender = request.POST['gender']
        student.address = request.POST['address']
        student.dob = request.POST['dob']
        student.full_clean()
        student.save()
        messages.success(request, "Student created successfully")
        return redirect('Student_show')
    return render(request, 'pages/Student/create.html')


def delete_by_id(request, id):
    students = Student.objects.get(pk=id)
    students.delete()
    messages.success(request, "Student deleted successfully")
    return redirect('Student_index')


def edit_by_id(request, id):
    students = Student.objects.get(pk=id)
    data = {"student": students}  # lowercase and singular
    return render(request, "pages/student/edit.html", context=data)


def update_by_id(request, id):
    student_existing = Student.objects.get(pk=id)
    student_existing.first_name = request.POST['first_name']
    student_existing.last_name = request.POST['last_name']
    student_existing.gender = request.POST['gender']
    student_existing.address = request.POST['address']
    student_existing.dob = request.POST['dob']
    student_existing.full_clean()
    student_existing.save()
    messages.success(request, "Student updated successfully")
    return redirect(f"/student/edit_by_id/{id}")
