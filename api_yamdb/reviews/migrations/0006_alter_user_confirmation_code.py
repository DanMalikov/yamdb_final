# Generated by Django 3.2 on 2023-02-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='код подтверждения'),
        ),
    ]
