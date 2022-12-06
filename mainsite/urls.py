from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('accounts/login/', views.login_page, name='login'),
    path('accounts/registration/', views.registration_page, name='registration'),
    path('accounts/logout/', views.logoutUser, name='logout'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('course/element/<int:pk>/', views.element_detail, name='element_detail'),
    path('course/create/', views.course_creation, name='course_creation'),
    path('element_creation/<int:pk>/', views.element_creation, name='element_creation')
]
