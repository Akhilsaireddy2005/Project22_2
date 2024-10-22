from django.shortcuts import render
from .models import Student
def home(request):
    return render(request,'home.html')
def insertData(request):
    n=request.POST['nameVar']
    a=request.POST['rollnoVar']
    Student.objects.create(name=n, rollno=a)
    students=Student.objects.all()
    return render(request,'home.html',{'students':students})
