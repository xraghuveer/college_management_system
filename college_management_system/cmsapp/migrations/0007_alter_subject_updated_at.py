# Generated by Django 4.1.7 on 2023-06-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0006_alter_subject_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]