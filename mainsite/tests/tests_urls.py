from django.test import SimpleTestCase, Client
from django.urls import reverse, resolve
from mainsite.views import *


class TestUrls(SimpleTestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'User'
        self.password = 'Test12345'
        

    def test_home_is_resolver(self):
        url = reverse('home_page')
        self.assertEquals(resolve(url).func, home_page)

    def test_login_is_resolver(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_page)

    def test_registration_is_resolver(self):
        url = reverse('registration')
        self.assertEquals(resolve(url).func, registration_page)

    def test_logout_is_resolver(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_coure_detail_is_resolver(self):
        url = reverse('course_detail', args=[1])
        self.assertEquals(resolve(url).func, course_detail)

    def test_element_detail_is_resolver(self):
        url = reverse('element_detail', args=[1])
        self.assertEquals(resolve(url).func, element_detail)

    def test_course_creation_is_resolver(self):
        url = reverse('course_creation')
        self.assertEquals(resolve(url).func, course_creation)

    def test_element_creation_is_resolver(self):
        url = reverse('element_creation', args=[1])
        self.assertEquals(resolve(url).func, element_creation) 