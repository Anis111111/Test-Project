# Generated by Django 5.0.6 on 2024-06-19 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='specialization',
            field=models.CharField(choices=[('networks', 'networks'), ('software', 'software')], default='software', max_length=50, verbose_name='specialization'),
        ),
    ]
