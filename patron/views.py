from django.shortcuts import render
from .models import MissingPerson
from django.http import HttpResponse

# Create your views here.
def personView(request,id):
    data_missingperson = MissingPerson.objects.get(id=id)
    context = {
        'data':data_missingperson,
    }
    return render(request, 'MissingPersonsProject1/person.html', context)

def indexPageView(request):
    return render(request, 'MissingPersonsProject1/index.html')

def about(request):
    return render(request, 'MissingPersonsProject1/about.html')

def contact(request):
    return render(request, 'MissingPersonsProject1/contact.html')

def current(request):
    data = MissingPerson.objects.all()
    context = {
        'data':data
    }
    return render(request, 'MissingPersonsProject1/current.html',context)

def post1(request):
    return render(request, 'MissingPersonsProject1/post.html')

def post2(request):
    return render(request, 'MissingPersonsProject1/post2.html')

def post3(request):
    return render(request, 'MissingPersonsProject1/post3.html')

def post4(request):
    return render(request, 'MissingPersonsProject1/post4.html')

