# Generated by Django 4.2 on 2023-10-05 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('year', models.IntegerField(default=2000)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='movies.director')),
            ],
        ),
    ]
