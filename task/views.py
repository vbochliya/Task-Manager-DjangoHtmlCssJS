from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from task.models import *
from datetime import datetime,date


def index(request):
    # print("index",'.....................................................................')
    return render(request,"index.html")

@login_required
def new_task(request):
    # print("new_task",'.....................................................................')
    if request.method == 'POST':
        title = request.POST.get('title')
        date_time = request.POST.get('date_time')
        date_time_target=datetime.strptime(date_time, '%Y-%m-%dT%H:%M')
        description = request.POST.get('description','')

        task_obj=all_the_tasks.objects.create(
            user=request.user,
            title=title,
            date_time_target=date_time_target,
            description=description,
            )
        task_obj.save()

    return render(request,"index.html")




@login_required
def completed_tasks(request):
    print("completed_tasks",'.....................................................................')
    task_obj=all_the_tasks.objects.filter(user=request.user,complete=True)
    context={"queryset":task_obj,
                "request_came_for":"completed_tasks"}

    return render(request,"index.html",context=context)

@login_required   
def pending_tasks(request):
    print("pending_tasks",'.....................................................................')
    task_obj=all_the_tasks.objects.filter(user=request.user,complete=False)
    context={"queryset":task_obj,
                "request_came_for":"pending_tasks"}

    return render(request,"index.html",context=context)


@login_required
def todays_tasks(request):
    print('todays_tasks','.....................................................................')
    task_obj = all_the_tasks.objects.filter(user=request.user,date_time_target__date=date.today())
    context={"queryset":task_obj,
                "request_came_for":"todays_tasks"}
    
    return render(request,"index.html",context=context)


@login_required
def complete_the_task(request):
    if request.method=="POST":
        task_id=request.POST.get("task_id")
        task_to_operate = get_object_or_404(all_the_tasks, id=task_id, user=request.user)
        task_to_operate.complete=True
        task_to_operate.save()

        return render(request,"index.html")
    
@login_required
def delete_the_task(request):
    if request.method=="POST":
        task_id=request.POST.get("task_id")
        task_to_operate = get_object_or_404(all_the_tasks, id=task_id, user=request.user)
        task_to_operate.delete()

        return render(request,"index.html")