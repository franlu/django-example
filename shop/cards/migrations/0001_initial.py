# Generated by Django 2.2.3 on 2019-07-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'db_table': 'tag',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('dtMod', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('kind', models.IntegerField(choices=[(1, 'bar'), (2, 'retail'), (3, 'other')], default=3, verbose_name='Type')),
                ('description', models.TextField(verbose_name='Description')),
                ('logo', models.ImageField(max_length=24576, upload_to='cards/logos', verbose_name='Logo')),
                ('image', models.ImageField(max_length=24576, upload_to='cards/img', verbose_name='Image')),
                ('tags', models.ManyToManyField(blank=True, to='cards.Tag', verbose_name='tags')),
            ],
            options={
                'db_table': 'card',
                'ordering': ('name',),
            },
        ),
    ]
