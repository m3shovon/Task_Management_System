# Generated by Django 4.2.1 on 2023-06-13 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Project', '0004_employeeproject_employeetask_employee_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignedtask',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='assignedtask',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='assignedtask',
            name='id',
        ),
        migrations.RemoveField(
            model_name='completedtask',
            name='completed_at',
        ),
        migrations.RemoveField(
            model_name='completedtask',
            name='completed_by',
        ),
        migrations.RemoveField(
            model_name='completedtask',
            name='id',
        ),
        migrations.RemoveField(
            model_name='incompletedtask',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='incompletedtask',
            name='id',
        ),
        migrations.RemoveField(
            model_name='workingtask',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='workingtask',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='workingtask',
            name='id',
        ),
        migrations.AlterField(
            model_name='assignedtask',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='App_Project.task'),
        ),
        migrations.AlterField(
            model_name='completedtask',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='App_Project.task'),
        ),
        migrations.AlterField(
            model_name='incompletedtask',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='App_Project.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='App_Project.project'),
        ),
        migrations.AlterField(
            model_name='workingtask',
            name='task',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='App_Project.task'),
        ),
    ]
