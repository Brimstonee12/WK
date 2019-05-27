# Generated by Django 2.1.4 on 2019-05-27 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190121_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_model_total',
            name='category',
            field=models.CharField(choices=[('N', 'News'), ('P', 'Politics'), ('S', 'Sport'), ('B', 'Business'), ('I', 'Other')], default='N', max_length=1),
        ),
    ]