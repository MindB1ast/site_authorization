# Generated by Django 4.1.4 on 2022-12-06 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_course_courseelement_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseelement',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainsite.course'),
        ),
    ]
