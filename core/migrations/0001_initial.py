# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=256)),
                ('prazo', models.DateTimeField(default=datetime.datetime(2015, 11, 11, 3, 18, 23, 183252, tzinfo=utc))),
                ('realizada', models.BooleanField()),
            ],
        ),
    ]
