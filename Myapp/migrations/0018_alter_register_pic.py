# Generated by Django 4.0.2 on 2022-03-21 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0017_department_uid_alter_register_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo1.jpg', upload_to='Profile Pic'),
        ),
    ]
