from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, ProblemForm
from .models import Problem
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')  # Corrected path

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('view_problems')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})  # Corrected path

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.user_type == 'Employee':
                return redirect('employee_dashboard')
            else:
                return redirect('view_problems')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})  # Corrected path

@login_required
def user_dashboard(request):
    problems = Problem.objects.filter(user=request.user)
    return render(request, 'view_problems.html', {'problems': problems})  # Corrected path

@login_required
def submit_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.mandal = request.user.mandal
            problem.district = request.user.district
            problem.save()
            return redirect('view_problems')
    else:
        form = ProblemForm()
    return render(request, 'submit_problem.html', {'form': form})  # Corrected path

@login_required
def employee_dashboard(request):
    problems = Problem.objects.all().order_by('-submission_date')
    
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('status_'):
                problem_id = key.split('_')[1]
                problem = Problem.objects.get(id=problem_id)
                problem.status = value
                problem.save()
        return redirect('employee_dashboard')
    
    return render(request, 'employee_dashboard.html', {'problems': problems})