from django.shortcuts import render


def home(request):
    return render(request, 'records/home.html')


def about(request):
    return render(request, 'records/about.html')


def attendance(request):
    return render(request, 'records/attendance.html')


def students(request):
    return render(request, 'records/students.html')


def contact(request):
    return render(request, 'records/contact.html')