# Generated by Django 2.0.3 on 2020-02-14 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('uploaded_date', models.DateField(auto_now=True)),
                ('genre', models.CharField(choices=[('Science fiction', 'Science fiction'), ('Satire', 'Satire'), ('Action and Adventure', 'Action and Adventure'), ('Romance', 'Romance'), ('Mystery', 'Mystery'), ('Horror', 'Horror'), ('Health', 'Health'), ('Guide', 'Guide'), ('Childrens', 'Childrens'), ('Religion, Spirituality & New Age', 'Religion, Spirituality & New Age'), ('Science', 'Science'), ('History', 'History'), ('Math', 'Math'), ('Poetry', 'Poetry'), ('Encyclopedias', 'Encyclopedias'), ('Dictionaries', 'Dictionaries'), ('Comics', 'Comics'), ('Art', 'Art'), ('Cook', 'Cook'), ('Diaries', 'Diaries'), ('Journals', 'Journals'), ('Trilogy', 'Trilogy'), ('Biographies', 'Biographies'), ('Fantasy', 'Fantasy'), ('Others', 'Others')], max_length=100)),
                ('positive_words', models.CharField(max_length=200)),
                ('negative_words', models.CharField(max_length=200)),
                ('total_words', models.IntegerField(default=0)),
                ('positive_words_count', models.IntegerField(default=0)),
                ('negative_words_count', models.IntegerField(default=0)),
                ('document', models.FileField(upload_to='doc/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbacksImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.IntegerField()),
                ('comments', models.CharField(max_length=200)),
                ('sentiments', models.CharField(default='no', max_length=200)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.Imag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
