# Generated by Django 5.1.1 on 2024-09-30 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0019_alter_periodictasks_options'),
        ('habbits', '0002_alter_habbit_reward_habbit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habbit',
            options={'verbose_name': 'Привычка', 'verbose_name_plural': 'Привычки'},
        ),
        migrations.AddField(
            model_name='habbit',
            name='name',
            field=models.CharField(default='lol', max_length=255, unique=True, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habbit',
            name='periodic_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='django_celery_beat.periodictask'),
        ),
    ]
