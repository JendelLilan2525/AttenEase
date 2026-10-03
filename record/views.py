from django.shortcuts import render
from .models import AttendanceRecord


def home(request):
    return render(request, 'records/home.html')


def about(request):
    return render(request, 'records/about.html')


def attendance(request):
    records = AttendanceRecord.objects.all().order_by('-date')
    return render(request, 'records/attendance.html', {'records': records})


def students(request):
    return render(request, 'records/students.html')


def contact(request):
    return render(request, 'records/contact.html')