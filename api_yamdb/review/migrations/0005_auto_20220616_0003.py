# Generated by Django 2.2.16 on 2022-06-15 21:03

from django.db import migrations, models
import review.validators


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_auto_20220616_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Укажите логин', max_length=100, unique=True, validators=[review.validators.validate_user], verbose_name='Логин'),
        ),
    ]