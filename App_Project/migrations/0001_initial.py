# Generated by Django 4.2.1 on 2023-05-14 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('employees', models.ManyToManyField(related_name='projects', to='App_User.employee')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managed_projects', to='App_User.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('ASSIGNED', 'Assigned'), ('WORKING', 'Working'), ('COMPLETED', 'Completed'), ('INCOMPLETED', 'Incompleted')], default='ASSIGNED', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ManyToManyField(related_name='assigned_tasks', to='App_User.employee')),
                ('completed_by', models.ManyToManyField(blank=True, related_name='completed_tasks', to='App_User.employee')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Project.project')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_User.employee')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Project.task')),
            ],
        ),
        migrations.CreateModel(
            name='IncompletedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Project.task')),
            ],
        ),
        migrations.CreateModel(
            name='CompletedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('completed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_User.employee')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Project.task')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_User.employee')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Project.task')),
            ],
        ),
    ]
