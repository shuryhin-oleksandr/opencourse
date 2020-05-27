# Generated by Django 3.0.5 on 2020-05-27 15:36

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200513_2133'),
        ('courses', '0003_auto_20200526_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandoutSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Handout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('attachment', models.FileField(upload_to='handouts/%Y-%m-%d/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.HandoutSection')),
            ],
            options={
                'verbose_name': 'Handout',
                'verbose_name_plural': 'Handout',
                'permissions': (('manage_handout', 'Manage handout'),),
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', autoslug.fields.AutoSlugField(unique=True)),
                ('accepted', models.NullBooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Student')),
            ],
            options={
                'verbose_name': 'Enrollment',
                'verbose_name_plural': 'Enrollment',
                'permissions': (('manage_enrollment', 'Manage enrollment'),),
            },
        ),
    ]
