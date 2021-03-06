# Generated by Django 3.2.9 on 2021-11-27 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_zona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=145)),
                ('slug', models.CharField(blank=True, max_length=45, null=True)),
                ('operator', models.CharField(blank=True, max_length=45, null=True)),
                ('type', models.CharField(blank=True, max_length=45, null=True)),
                ('description', models.CharField(max_length=256)),
                ('img', models.CharField(blank=True, max_length=256, null=True)),
                ('pais', models.CharField(blank=True, max_length=45, null=True)),
                ('zonaLlegada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours_llegada', to='tours.zona')),
                ('zonaSalida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours_salida', to='tours.zona')),
            ],
        ),
    ]
