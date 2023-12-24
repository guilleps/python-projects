from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Welcome to my Home Page'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username, id):
    return HttpResponse('Hello %s y %i' % (username,id))

def about(request):
    username = 'guillermo'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

# def projects(request):
#     projects = list(Project.objects.values())
#     return JsonResponse(projects, safe=False)




def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

# def tasks(request, id):
#     # tasks = Task.objects.get(id = id)
#     tasks = get_object_or_404(Task, id = id)
#     return HttpResponse('task: %s' % tasks.title)

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'], 
                            project_id=2)
        return redirect('tasks')
    

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
        'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')