# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_id',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='author_name',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
