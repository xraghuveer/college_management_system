# Generated by Django 4.1.7 on 2023-07-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0008_alter_subject_created_at_alter_subject_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
