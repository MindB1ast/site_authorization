from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from .forms import AdditionalUserForm, ElementCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
from mainsite.models import Course, CourseElement
from loguru import logger


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        form = AdditionalUserForm()

        if request.method == 'POST':
            form = AdditionalUserForm(request.POST) 
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {'form':form}
        return render(request, 'mainsite/auth/registration.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    else:    
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            logger.debug(email)
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user:
                login(request, user)
                return redirect('home_page')

        context = {}
        return render(request, 'mainsite/auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home_page')


@login_required
def home_page(request):
    user = User.objects.get( id=request.user.id)
    courses = Course.objects.all()
    context = {
        'courses': courses, 
        'user': user,
    }
    return render(request, 'mainsite/home_page.html', context)


@login_required
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user =  User.objects.get(id=request.user.id)
    elements = CourseElement.objects.filter(course=course)
    context = {
        'elements': elements,
        'course': course,
        'user': user,
        }
    return render(request, 'mainsite/courses_detail.html', context)


@login_required
def element_creation(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = ElementCreationForm()
    if request.method == 'POST':
        form = ElementCreationForm(request.POST)
        if form.is_valid():
            form.save()
            element = CourseElement.objects.get(
                    name=request.POST.get('name'),
                    text=request.POST.get('text')
                )
            element.course = course
            element.save()
            return redirect('course_detail',pk)

    context = {
        'form':form
    }

    return render(request, 'mainsite/element_creation.html', context)


@login_required
def element_detail(request, pk):
    element = get_object_or_404(CourseElement, pk=pk)
    context = {'element': element}
    return render(request, 'mainsite/element_detail.html', context)


@login_required
def course_creation(request):
    users = User.objects.all()
    if request.method == "POST":
        course = Course.objects.create(
            name = request.POST.get("name") 
        )

        for user in users:
            if request.POST.get(user.email):
                course.user.add(User.objects.get(id=request.POST.get(user.email)))
        return redirect('home_page')

    context = {
        'users': users 
        }
    return render(request, 'mainsite/course_creation.html',context)


