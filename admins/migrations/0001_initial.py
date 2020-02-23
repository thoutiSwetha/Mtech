# Generated by Django 2.0.3 on 2020-02-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uploaded_date', models.DateField(auto_now=True)),
                ('genre', models.CharField(choices=[('Aerial', 'Aerial'), ('Architectural', 'Architectural'), ('Candid', 'Candid'), ('Documentary', 'Documentary'), ('Fashion', 'Fashion'), ('Food', 'Food'), ('Landscape', 'Landscape'), ('Photojournalism', 'Photojournalism'), ('Conceptual/ fine art', 'Conceptual/ fine art'), ('Portraiture', 'Portraiture'), ('Sport', 'Sport'), ('War', 'War'), ('Wildlife', 'Wildlife'), ('Paintings', 'Paintings'), ('others', 'others')], max_length=100)),
                ('sentiment', models.CharField(default='no', max_length=200)),
                ('overallratings', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('images', models.FileField(upload_to='img/')),
            ],
        ),
    ]