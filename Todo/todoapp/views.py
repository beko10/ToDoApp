from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo
# Create your views here.


def index(request):
    todos = Todo.objects.all()
    contex={
        "todos":todos
    }    
    return render(request,"index.html",contex)

def TodoAdd(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        contex = form.cleaned_data.get("contex")

        newTodo = Todo(title=title,contex=contex)
        messages.success(request,"Todo başarılı bir şekilde eklendi")
        newTodo.save()
        return redirect("index")
    contex = {
        "form":form
    }
    return render(request,"todoadd.html",contex)

def TodoDelete(request,id):
    todo = get_object_or_404(Todo,pk=id)
    messages.error(request,"todo başarıyla silindi ... ")
    todo.delete()
    return redirect("index")

def TodoDetail(request,id):
    todo = get_object_or_404(Todo,pk=id)
    return render(request,"detail.html",{"todo":todo})

def TodoUpdate(request,id):
    todo = Todo.objects.get(pk=id)
    if request.method == "POST":
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            messages.success(request,"todo başarılı bir şekilde guncellendi")
            todo.save()
            return redirect("index")
    else:
        form = TodoForm(instance=todo)
    return render(request,"update.html",{"form":form})



def TodoCompleted(request,id):
    todo = Todo.objects.get(pk=id)
    todo.completed = True
    messages.success(request,"todo tamamlandı olarak işaretlendi ... ")
    todo.save()
    return redirect("index")



"""



    if request.method == "POST":
        query = request.POST.get("q")
        results = []
        results = Todo.objects.filter(title__icontains=query)
        print(results)
        return render(request,"searchresult.html",{"results":results})
    return redirect("index")
"""


