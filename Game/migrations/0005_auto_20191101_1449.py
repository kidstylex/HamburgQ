# Generated by Django 2.2.5 on 2019-11-01 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0004_waitingroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitingroom',
            name='quiz_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Game.Quiz'),
        ),
        migrations.AddField(
            model_name='waitingroom',
            name='time',
            field=models.IntegerField(default='0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='waitingroom',
            name='room_id',
            field=models.IntegerField(unique=True),
        ),
    ]
