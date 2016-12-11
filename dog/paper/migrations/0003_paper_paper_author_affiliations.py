# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0002_auto_20161211_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paper_id', models.CharField(max_length=20)),
                ('original_title', models.CharField(max_length=50)),
                ('normalized_title', models.CharField(max_length=50)),
                ('publish_year', models.IntegerField()),
                ('publish_date', models.DateTimeField()),
                ('DOI', models.CharField(max_length=50)),
                ('original_venue_name', models.CharField(max_length=50)),
                ('normalized_venue_name', models.CharField(max_length=50)),
                ('jornal_id', models.CharField(max_length=50)),
                ('conference_id', models.CharField(max_length=50)),
                ('paper_rank', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paper_Author_Affiliations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affiliation_id', models.CharField(max_length=50)),
                ('original_affiliation_name', models.CharField(max_length=50)),
                ('normalized_affiliation_name', models.CharField(max_length=50)),
                ('author_sequence_number', models.CharField(max_length=50)),
                ('author', models.ForeignKey(to='paper.Author')),
                ('paper', models.ForeignKey(to='paper.Paper')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
