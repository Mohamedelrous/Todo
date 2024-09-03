from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Add this import
from .models import Task, Category
from .forms import TaskForm, CategoryForm

# Home page for guests or redirect to dashboard if authenticated
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'main/home.html')

@login_required
def dashboard(request):
    tasks = Task.objects.all().order_by('due_date')
    categories = Category.objects.all()
    context = {'tasks': tasks, 'categories': categories}
    return render(request, 'main/index.html', context)

def detailed_task(request, id):
    task = get_object_or_404(Task, id=id)
    context = {'task': task}
    return render(request, 'main/detailed.html', context)

def todo_by_status(request, st):
    todos = Task.objects.filter(status=st)
    context = {'todos': todos}
    return render(request, 'main/todosstatus.html', context)

def Todo_list_Category(request, id):
    todos = Task.objects.filter(category=id)
    categories = Category.objects.all()
    context = {'tasks': todos, 'categories': categories}
    return render(request, 'main/index.html', context)

def Createtodo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'main/create_todo.html', {'form': form})

def createCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'main/createCategorys.html', {'form': form})

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'main/updatetask.html', {'form': form})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'main/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')
