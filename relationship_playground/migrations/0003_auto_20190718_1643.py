# Generated by Django 2.2.3 on 2019-07-18 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_playground', '0002_pizza_topping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('societies', models.ManyToManyField(through='relationship_playground.Membership', to='relationship_playground.Society')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationship_playground.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='society_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationship_playground.Society'),
        ),
    ]
