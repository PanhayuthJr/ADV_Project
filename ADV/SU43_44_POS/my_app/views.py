from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={"Name":"CoCa"}
    return render(request, "index.html",context=data)
def find_by_id(request,id):
    return HttpResponse(f"id{id}")

def contact(request):
    return render(request,"pages/content.html")
