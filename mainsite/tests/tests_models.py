from django.test import TestCase
from django.contrib.auth.models import User
from mainsite.models import Course, CourseElement


class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            username='Eldar',
        )
        self.user2 = User.objects.create(
            username='Nikita'
        )

        self.course1 = Course.objects.create(
            name='Программирование',
        )

        self.course2 = Course.objects.create(
            name='Медицина',
        )

        self.course1.user.add(self.user1)
        self.course2.user.add(self.user2)

        self.element1 = CourseElement.objects.create(
            name='Элемент1',
            text='Тестовый текст1',
            course = self.course1
        )

        self.element2 = CourseElement.objects.create(
            name='Элемент2',
            text='Тестовый текст2',
            course = self.course2
        )

    def test_course_creation(self):
        courses = Course.objects.all()
        count=0
        for course in courses:
            count+=1
        test = Course.objects.get(name='Программирование')
        self.assertEquals(test.name, 'Программирование')
        self.assertEquals(count,2)

    def test_element_creation(self):
        element1 = CourseElement.objects.get(name='Элемент1')
        element2 = CourseElement.objects.get(name='Элемент2')

        counter=0
        elements = CourseElement.objects.all()
        for element in elements:
            counter+=1

        self.assertEquals(element1.text, 'Тестовый текст1')
        self.assertEquals(element2.text, 'Тестовый текст2')
        self.assertEquals(counter,2)