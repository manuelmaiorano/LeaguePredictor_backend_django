# Generated by Django 4.1.7 on 2023-03-27 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeagueProbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='LeagueRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=20)),
                ('wins', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('probab', models.FloatField()),
                ('league_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.leagueprobs')),
            ],
        ),
    ]
