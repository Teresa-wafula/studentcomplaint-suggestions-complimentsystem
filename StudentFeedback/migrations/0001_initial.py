# Generated by Django 5.0.3 on 2024-03-25 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BullyingComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('rape', 'Rape Complaint'), ('sexual_misconduct', 'Sexual Misconduct Complaint'), ('bullying', 'Bullying Complaint'), ('harassment', 'Harassment Complaint')], max_length=20)),
                ('date', models.DateField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('evidence', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('rape', 'Rape Complaint'), ('sexual_misconduct', 'Sexual Misconduct Complaint'), ('bullying', 'Bullying Complaint'), ('harassment', 'Harassment Complaint')], max_length=20)),
                ('date', models.DateField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('evidence', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HarassmentComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('rape', 'Rape Complaint'), ('sexual_misconduct', 'Sexual Misconduct Complaint'), ('bullying', 'Bullying Complaint'), ('harassment', 'Harassment Complaint')], max_length=20)),
                ('date', models.DateField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('evidence', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RapeComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('rape', 'Rape Complaint'), ('sexual_misconduct', 'Sexual Misconduct Complaint'), ('bullying', 'Bullying Complaint'), ('harassment', 'Harassment Complaint')], max_length=20)),
                ('date', models.DateField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('evidence', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SexualMisconductComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('rape', 'Rape Complaint'), ('sexual_misconduct', 'Sexual Misconduct Complaint'), ('bullying', 'Bullying Complaint'), ('harassment', 'Harassment Complaint')], max_length=20)),
                ('date', models.DateField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('evidence', models.FileField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password1', models.CharField(max_length=255)),
                ('password2', models.CharField(max_length=255)),
            ],
        ),
    ]
