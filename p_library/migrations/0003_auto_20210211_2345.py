# Generated by Django 2.2.6 on 2021-02-11 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20210211_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Friend', verbose_name='Другу отдана'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='full_name',
            field=models.TextField(verbose_name='Имя'),
        ),
    ]
