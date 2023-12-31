# Generated by Django 4.2.4 on 2023-08-19 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Frontend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=250)),
                ('Mobile', models.CharField(max_length=250)),
                ('Projectname', models.CharField(max_length=250)),
                ('Desciption', models.TextField(max_length=250)),
                ('Backendend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideacollector.backend')),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideacollector.course')),
                ('Framework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideacollector.framework')),
                ('Frontend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideacollector.frontend')),
            ],
        ),
    ]
