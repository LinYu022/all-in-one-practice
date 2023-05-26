# Generated by Django 3.2 on 2023-05-23 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tb_student',
            fields=[
                ('sid', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
                ('bjid', models.IntegerField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tb_teacher',
            fields=[
                ('tid', models.IntegerField(max_length=3, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('tname', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('email', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]