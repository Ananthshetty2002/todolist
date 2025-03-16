from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Task,Category
from .forms import TaskForm,CategoryForm
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.\
def task_list(request):
    query = request.GET.get("q", "") 
    if query:
        tasks = Task.objects.filter(title__icontains=query)  
    else:  
        tasks = Task.objects.all()  
    return render(request, "task_list.html", {"tasks": tasks})
@login_required
def task_create(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm()
    return render(request,'task_form.html',{'form':form})


@login_required
def task_update(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form=TaskForm(instance=task)
        return render(request,TaskForm,{'form':form})
        
@login_required
def task_delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')

@login_required
def category_create(request):
    if request.method=='POST':
      form=CategoryForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('category_list')
    else:
      form=CategoryForm()
      return render(request,'category_form.html',{'form':form})
          
def signup(request):
    if request.method=='POST':
      form=UserCreationForm(request.POST)
      if form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('home') 
    else:
       form=UserCreationForm()
       return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("task_list")  
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")  

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")  
    
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed 
    task.save()
    print(f"New status: {task.completed}") 
    return redirect('task_list')  
    
@login_required
def category_list(request):
    categories = Category.objects.all()  
    return render(request, 'category_list.html', {'categories': categories}) 

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            return redirect("task_list") 
        else:
            messages.error(request, "Invalid username or password.") 
    return render(request, "login.html")  

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def delete(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('task_list')