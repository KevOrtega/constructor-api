# Generated by Django 4.2.3 on 2023-07-25 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_first_name_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(auto_created=True, blank=True, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
