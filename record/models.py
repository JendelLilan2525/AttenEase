from django.db import models


class AttendanceRecord(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student_name} - {self.date}"