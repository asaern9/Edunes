# Generated by Django 2.2.1 on 2019-08-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_unapprovednews'),
    ]

    operations = [
        migrations.AddField(
            model_name='unapprovednews',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='Unapproved/'),
        ),
    ]