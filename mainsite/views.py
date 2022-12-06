from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from .forms import AdditionalUserForm, ElementCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
from mainsite.models import Course, CourseElement

def registration_page(request):
    form = AdditionalUserForm()

    if request.method == 'POST':
        form = AdditionalUserForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'mainsite/auth/registration.html', context)


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
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


def element_creation(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = ElementCreationForm()
    if request.method == "POST":
        form = ElementCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('course_detail')

    context = {
        'form':form
    }

    return render(request, 'mainsite/element_creation.html', context)

def element_detail(request, pk):
    element = get_object_or_404(CourseElement, pk=pk)
    context = {'element': element}
    return render(request, 'mainsite/element_detail.html', context)



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


