# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 23:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Testings', '0012_remove_testcase_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('script', models.TextField(blank=True, verbose_name='script')),
                ('values', models.TextField(blank=True, verbose_name='values')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('collection', models.ManyToManyField(to='Testings.Collection')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'test suite',
                'verbose_name_plural': 'test suites',
                'db_table': 'testsuites',
            },
        ),
        migrations.AlterModelOptions(
            name='testcase',
            options={'verbose_name': 'test case', 'verbose_name_plural': 'test cases'},
        ),
    ]
