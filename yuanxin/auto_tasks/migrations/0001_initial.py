# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-09 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('playbook', models.FileField(upload_to='playbook/%Y/%m', verbose_name='playbook\u6587\u4ef6')),
                ('detail_result', models.TextField(verbose_name='\u6267\u884c\u7ed3\u679c\u8be6\u60c5')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='\u4efb\u52a1\u521b\u5efa\u65f6\u95f4')),
                ('exec_time', models.DateTimeField(auto_now=True, verbose_name='\u6267\u884c\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1',
                'verbose_name_plural': '\u4efb\u52a1',
            },
        ),
        migrations.CreateModel(
            name='ExecResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=64, verbose_name='\u4e3b\u673a\u540d')),
                ('unreachable', models.IntegerField(verbose_name='\u4e0d\u53ef\u8fbe')),
                ('skipped', models.IntegerField(verbose_name='\u8df3\u8fc7')),
                ('ok', models.IntegerField(verbose_name='\u6210\u529f')),
                ('changed', models.IntegerField(verbose_name='\u6539\u53d8')),
                ('failures', models.IntegerField(verbose_name='\u5931\u8d25')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_tasks.AutoTasks', verbose_name='\u4efb\u52a1')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u7ed3\u679c',
                'verbose_name_plural': '\u4efb\u52a1\u7ed3\u679c',
            },
        ),
    ]
