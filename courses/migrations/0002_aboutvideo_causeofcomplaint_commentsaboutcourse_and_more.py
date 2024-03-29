# Generated by Django 5.0.1 on 2024-01-31 10:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comments', models.IntegerField()),
                ('number_of_views', models.IntegerField()),
                ('number_of_likes', models.IntegerField()),
                ('language', models.CharField(max_length=100)),
                ('video_duration', models.DurationField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CauseOfComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('complaint_type', models.CharField(choices=[('1', "No-o'rin savol/izoh"), ('2', 'Insonning shaniga teguvchi gaplar'), ('3', "Boshqalarga nisbatan so'kish va haqorat qiluvchi leksika"), ('4', "Terrorizmga da'vat"), ('5', "Tushunarsiz va umuman kerak bo'lmagan izoh"), ('6', 'Boshqa')], max_length=100)),
                ('other_description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentsAboutCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('overall_rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('overall_comments', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('rated_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentsAboutVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('comment', models.TextField()),
                ('left_comment', models.DateTimeField(auto_now_add=True)),
                ('my_comment', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('title_of_video', models.CharField(max_length=100)),
                ('short_content', models.TextField()),
                ('liked', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='media/')),
                ('received_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NPVideoCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('title_for_content', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('facebook_url', models.URLField()),
                ('telegram_url', models.URLField()),
                ('copy_link_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=255)),
                ('card_number', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(16, message='The field must not exceed 16 digits. ')])),
                ('validity_period', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(4, message='The field must not exceed 16 digits. ')])),
                ('CVV', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(3, message='The field must not exceed 16 digits. ')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RateCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment_about_course', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsefulResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tasklist', models.FileField(upload_to='')),
                ('youtube_tutorial_url', models.URLField()),
                ('image', models.ImageField(upload_to='media/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('duration', models.DurationField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_type', models.CharField(choices=[('payme', 'Payme'), ('apelsin', 'Apelsin'), ('click', 'CLICK'), ('uzcard', 'UZCARD'), ('visa', 'VISA'), ('mastercard', 'mastercard')], max_length=100)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.videocourse')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('number_of_videous', models.IntegerField()),
                ('total_duration', models.DurationField()),
                ('status', models.CharField(choices=[('in_prog', 'Jarayonda'), ('np', 'Sotib olinmagan'), ('com', "Ko'rilgan"), ('not_seen', "Ko'rilmagan")], default='np', max_length=25)),
                ('videos', models.ManyToManyField(to='courses.video')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
