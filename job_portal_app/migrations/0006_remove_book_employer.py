# Generated by Django 4.2.2 on 2023-06-17 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0005_rename_user_book_jobseeker_rename_user_job_employer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='employer',
        ),
    ]