# Generated by Django 3.2.7 on 2021-09-30 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('a', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queries.a')),
            ],
        ),
        migrations.CreateModel(
            name='C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queries.a')),
            ],
        ),
        migrations.RemoveField(
            model_name='pc',
            name='model',
        ),
        migrations.RemoveField(
            model_name='printer',
            name='model',
        ),
        migrations.DeleteModel(
            name='Laptop',
        ),
        migrations.DeleteModel(
            name='PC',
        ),
        migrations.DeleteModel(
            name='Printer',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]