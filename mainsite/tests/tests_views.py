from django.test import TestCase, Client
from django.urls import reverse
from mainsite.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.register_url=reverse('registration')
        self.login_url=reverse('login')
        self.user={
            'email':'testemail@gmail.com',
            'username':'username',
            'password':'password',
            'password2':'password',
            'first_name':'fullname',
            'last_name':'lastname'
        }

        return super().setUp()


class RegisterTest(TestViews):
   def test_can_view_page_correctly(self):
       response=self.client.get(self.register_url)
       self.assertEqual(response.status_code,200)
       self.assertTemplateUsed(response,'mainsite/auth/registration.html')

   def test_can_register_user(self):
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)


class LoginTest(TestViews):
    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'mainsite/auth/login.html')

    def test_login_success(self):
        self.client.post(self.register_url,self.user,format='text/html')
        user=User.objects.get_or_create(email=self.user['email'])[0]
        user.save()
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,200)