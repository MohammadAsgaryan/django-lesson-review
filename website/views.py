from django.shortcuts import render, redirect
from website.models import Contact
from .forms import ContactModelform, NewslatterForm
from django.http import HttpResponse,JsonResponse
from django.http.response import HttpResponseRedirect

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method=="POST":
        form = ContactModelform(request.POST)
        if form.is_valid():
            form.save()
    form = ContactModelform()
    return render(request, 'website/contact.html', {'form': form})
    
def newslatter_view(request):
    if request.method=='POST':
        form = NewslatterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')