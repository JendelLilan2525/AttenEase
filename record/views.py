from django.shortcuts import render, redirect
from .models import AttendanceRecord


def home(request):
    return render(request, 'records/home.html')


def about(request):
    return render(request, 'records/about.html')


def attendance(request):

    if request.method == 'POST':

        student_name = request.POST['student_name']
        student_id = request.POST['student_id']
        date = request.POST['date']
        status = request.POST['status']

        AttendanceRecord.objects.create(
            student_name=student_name,
            student_id=student_id,
            date=date,
            status=status
        )

        return redirect('attendance')

    records = AttendanceRecord.objects.all().order_by('-date')

    return render(
        request,
        'records/attendance.html',
        {'records': records}
    )


def students(request):

    students = AttendanceRecord.objects.all().order_by('student_name')

    return render(
        request,
        'records/students.html',
        {'students': students}
    )


def contact(request):
    return render(request, 'records/contact.html')