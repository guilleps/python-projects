from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request, username, id):
    return HttpResponse('Hello %s y %i' % (username,id))

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

# def projects(request):
#     projects = list(Project.objects.values())
#     return JsonResponse(projects, safe=False)




def tasks(request):
    return render(request, 'tasks.html')

# def tasks(request, id):
#     # tasks = Task.objects.get(id = id)
#     tasks = get_object_or_404(Task, id = id)
#     return HttpResponse('task: %s' % tasks.title)