from django.shortcuts import render
from .models import Student

def testmysql(request):
    student = Student.objects.all()  

    if student.exists(): 
        context = {
            'student_id': student[0].student_id,  
            'student_name': f"{student[0].first_name} {student[0].last_name}", 
        }
    else:
        context = {
            'student_id': 'N/A',
            'student_name': 'No Students Found',
        }

    return render(request, 'home.html', context)
