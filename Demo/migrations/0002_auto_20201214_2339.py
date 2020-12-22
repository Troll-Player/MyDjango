# Generated by Django 2.2 on 2020-12-14 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub',
            field=models.ForeignKey(blank=True, db_column='pid', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book', to='Demo.Publisher'),
        ),
    ]
