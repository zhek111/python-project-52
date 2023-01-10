# Generated by Django 4.1.5 on 2023-01-10 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0003_rename_statuses_status'),
        ('labels', '0003_rename_labels_label'),
        ('tasks', '0006_alter_tasklabel_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.TaskLabel', to='labels.label', verbose_name='labels'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='statuses.status', verbose_name='status'),
        ),
    ]