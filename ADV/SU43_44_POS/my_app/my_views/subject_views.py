from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from my_app.models import Subject


# -------------------- Subject Views --------------------

def index(request):
    if request.method == "POST":
        subject = Subject()
        subject.subject_name = request.POST['search_item']
        subject = Subject.objects.filter(name=subject.subject_name)
        paginator = Paginator(subject, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {"subject": page_obj, "count_items": (subject.count())}
    else:
        search_query = request.GET.get('search_item', '')  # <-- added search
        if search_query:
            subject = Subject.objects.filter(name__icontains=search_query)
        else:
            subject = Subject.objects.all()
        paginator = Paginator(subject, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        data = {"subject": page_obj, "count_items": (subject.count())}

    return render(request, "pages/Subject/index.html", context=data)
def show(request):
    return render(request, "pages/Subject/create.html")
def create(request):
    if request.method == 'POST':
        subject = Subject()
        subject.name = request.POST['name']  # Correct field
        subject.full_clean()  # optional validation
        subject.save()
        if subject.pk:
            messages.success(request, "Subject created successfully")
        return redirect('Subject_index')  # Usually redirect to list
    else:
        return render(request, 'pages/Subject/create.html')
def delete_by_id(request,id):
    subject = Subject.objects.get(pk=id)
    subject.delete()
    messages.success(request, "Subject deleted successfully")
    return redirect('Subject_index')
def edit_by_id(request,id):
    subject = Subject.objects.get(pk=id)
    data = {"subject": subject}
    return render(request, "pages/Subject/edit.html", context=data)
def update_by_id(request, id):
    subject_existing = Subject.objects.get(pk=id)
    subject_existing.name = request.POST['name']
    subject_existing.full_clean()
    subject_existing.save()
    messages.success(request, "Subject updated successfully")
    return redirect(f"/Subject/edit_by_id/{id}")