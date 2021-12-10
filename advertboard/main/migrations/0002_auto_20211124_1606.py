# Generated by Django 3.2.9 on 2021-11-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ('name',), 'verbose_name': 'Название', 'verbose_name_plural': 'Названия'},
        ),
        migrations.RemoveField(
            model_name='ad',
            name='created',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='updated',
        ),
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.CharField(db_index=True, max_length=100, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, upload_to='ads/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
    ]