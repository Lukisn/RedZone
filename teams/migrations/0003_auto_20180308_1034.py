# Generated by Django 2.0.3 on 2018-03-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20180308_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='home_city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='home_country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('C', 'Center'), ('OL', 'Offensive line'), ('OG', 'Offensive guard'), ('OT', 'Offensive tackle'), ('QB', 'Quarterback'), ('RB', 'Running back'), ('WR', 'Wide receiver'), ('TE', 'Tight end'), ('DL', 'Defensive line'), ('DT', 'Defensive tackle'), ('DE', 'Defensive end'), ('DB', 'Defensive back'), ('MLB', 'Middle line backer'), ('LB', 'Line backer'), ('CB', 'Corner back'), ('S', 'Safety')], max_length=50),
        ),
    ]
