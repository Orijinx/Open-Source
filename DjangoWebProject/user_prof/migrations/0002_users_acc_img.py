# Generated by Django 2.2.5 on 2019-12-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_prof', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='acc_img',
            field=models.ImageField(default='Soso', upload_to=''),
            preserve_default=False,
        ),
    ]
