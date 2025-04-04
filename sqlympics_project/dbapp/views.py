from django.shortcuts import render
from django.http import JsonResponse
from .chatbot import get_sql_query, execute_sql

def index(request): return render(request, 'dbapp/index.html')
def student_login(request): return render(request, 'dbapp/student_login.html')
def student_dashboard(request): return render(request, 'dbapp/student_dashboard.html')
def instructor_login(request): return render(request, 'dbapp/instructor_login.html')
def instructor_dashboard(request): return render(request, 'dbapp/instructor_dashboard.html')
def register(request): return render(request, 'dbapp/register.html')

def chatbot(request):
    prompt = request.GET.get("prompt", "")
    if not prompt:
        return JsonResponse({"error": "Empty prompt"})
    try:
        sql = get_sql_query(prompt)
        result = execute_sql(sql)
        return JsonResponse({"sql": sql, "result": result})
    except Exception as e:
        return JsonResponse({"error": str(e)})
