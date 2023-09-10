from django.shortcuts import render
from app.forms import *
from app.models import *
# Create your views here.


def insert_student(request):
    SFEO = StudentForm()
    if request.method == 'POST':
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            Sname = SFDO.cleaned_data['Sname']
            Sid = SFDO.cleaned_data['Sid']
            Semail = SFDO.cleaned_data['Semail']

            so = Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            so.save()
            
            QSSO = Student.objects.all()
            return render(request,'display_student.html',{'QSSO':QSSO})

    return render(request,'insert_student.html',{'SFEO':SFEO})