# Generated by Django 4.1.7 on 2023-02-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buniwacreations', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='facts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('happy_clients', models.TextField()),
                ('projects_done', models.TextField()),
                ('awards', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]