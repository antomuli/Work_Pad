from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from django.contrib.auth import logout
from .models import *
# Create your views here.
@login_required(login_url = '/accounts/login/')
def home(request):
    '''
    View function to render thr home page
    '''
    # user=request.User()
    return render(request,'home.html',)
@login_required(login_url = '/accounts/login/')
@permission_required("True","home")
def registered_users(request):
    users=User.objects.all()
    context={
    'users':users,
    }
    return render(request,'admin_site/users.html',context)
@login_required(login_url = '/accounts/login/')
@permission_required("True","home")
def user_deactivate(request,id):
    user=User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.success(request,f"{user.firstname}'s account has been deactivated'")
    return redirect('system_users')
@login_required(login_url = '/accounts/login/')
@permission_required("True","home")
def user_activate(request,user_id):
    user=User.objects.get(id=user_id)
    user.is_active=True
    user.save()
    messages.success(request,f"{user.firstname}'s account is now activated'")
    return redirect('system_users')
@login_required(login_url = '/accounts/login/')
@permission_required("True","home")
def dashboard(request):
    return render(request,'admin_site/dashboard.html')
@login_required(login_url = '/accounts/login/')
@permission_required("True","home")
    def assign_task(request):
    if request.method=='POST':
        form = assignTaskForm(request.POST,request.FILES)
        if form.is_valid():
            task=form.save(commit=False)
            task.due_date = request.POST.get('due_on')
            task.save()
            return redirect('system_users')
        else:
            form=assignTaskForm()
        return render(request,'admin_site/assign_task.html',{'form':form})
@login_required(login_url = '/accounts/login/')
@permission_required("True","home")
def rate(request,id):
    if request.method == 'POST':
        rates = kpis.objects.filter(id=id)
        rates_for= request.user
        work_quality=request.POST.get('work_quality')
        attendance=request.POST.get('attendance')
        punctuality=request.POST.get('punctuality')
        soft_skills=request.POST.get('soft_skills')

        if work_quality and attendance and punctuality and soft_skills:
            user=User.objects.get(id=id)
            rate = kpis(work_quality=work_quality,attendance=attendance,punctuality=punctuality,soft_skills=soft_skills,rates_for=user)
            rate.save()
            messages.info(request,'User rated succesfully!')
            return redirect('system_users')
        else:
            messages.info(request,'Make sure all fields are filled')
            return redirect('system_users')
    else:
        form=rateEmployeeForm()
        messages.info(request,'Make sure all fields are filled')
        return redirect('system_users')
@login_required(login_url = '/accounts/login/')
def profile(request):
    my_tasks = tasks.objects.filter(assigned_to = request.user)
    rates=kpis.objects.filter(rates_for=request.user)
    work_quality_rate=[]
    attendance_rate=[]
    punctuality_rate=[]
    soft_skills_rate=[]
    if rates:
        for rate in rates:
            work_quality_rate.append(rate.work_quality)
            attendance_rate.append(rate.attendance)
            punctuality_rate.append(rate.punctuality)
            soft_skills_rate.append(rate.soft_skills)

        total = len(work_quality_rate)*10
        work_quality = round(sum(work_quality_rate)/total *100,1)
        attendance = round(sum(attendance_rate)/total*100,1)
        punctuality = round(sum(punctuality_rate)/total*100,1)
        soft_skills=round(sum(soft_skills_rate)/total*100,1)
        overall=round((work_quality+punctuality+attendance+soft_skills)/4,1)
        return render(request,'profile.html',{'my_tasks':my_tasks,'work_quality':work_quality,'attendance':attendance,'punctuality':punctuality,'soft_skills':soft_skills,'overall':overall})
    else:
        work_quality = 0
        attendance = 0
        punctuality = 0
        soft_skills = 0
        return render(request,'profile.html',{'my_tasks':my_tasks,'work_quality':work_quality,'attendance':attendance,'punctuality':punctuality,'soft_skills':soft_skills})
@login_required(login_url="/accounts/login/")
def logout_request(request):
    '''
    Function for logging out user
    '''
    logout(request)
    return redirect('home')