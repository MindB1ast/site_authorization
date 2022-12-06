# Generated by Django 4.1.4 on 2022-12-06 13:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainsite', '0004_usercourserelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourserelation',
            name='course',
            field=models.ManyToManyField(blank=True, to='mainsite.course'),
        ),
        migrations.AlterField(
            model_name='usercourserelation',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]