# Generated by Django 3.2.4 on 2021-06-19 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('age', models.IntegerField(default=0, max_length=2)),
                ('exact_age', models.BooleanField(default=False)),
            ],
        ),
    ]
