# Generated by Django 2.2 on 2020-12-14 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'publisher',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(blank=True, max_length=200, null=True)),
                ('pub', models.ForeignKey(blank=True, db_column='pid', on_delete=django.db.models.deletion.PROTECT, related_name='book', to='Demo.Publisher')),
            ],
            options={
                'db_table': 'book',
                'managed': True,
            },
        ),
    ]
