# Generated by Django 3.0.7 on 2020-06-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0065_auto_20200626_1444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['order', 'pk']},
        ),
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['order', 'pk']},
        ),
        migrations.AddField(
            model_name='step',
            name='name',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
