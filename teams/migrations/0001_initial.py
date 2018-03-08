# Generated by Django 2.0.3 on 2018-03-08 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('home_country', models.CharField(max_length=50)),
                ('home_city', models.CharField(max_length=50)),
                ('number', models.PositiveSmallIntegerField()),
                ('position', models.CharField(choices=[('C', 'Center'), ('OG', 'Offensive guard'), ('OT', 'Offensive tackle'), ('QB', 'Quarterback'), ('RB', 'Running back'), ('WR', 'Wide receiver'), ('TE', 'Tight end'), ('DT', 'Defensive tackle'), ('DE', 'Defensive end'), ('MLB', 'Middle line backer'), ('LB', 'Line backer'), ('CB', 'Corner back'), ('S', 'Safety')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
                ('home_city', models.CharField(max_length=50)),
                ('home_page', models.SlugField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Team'),
        ),
    ]