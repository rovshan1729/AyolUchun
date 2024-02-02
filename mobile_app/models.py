from django.db import models
from courses.models import BaseModel
from django.core.validators import MinValueValidator,MaxValueValidator



class Category(BaseModel):
    title = models.CharField(max_length=64)
    total = models.IntegerField()

    def __str__(self):
        return self.title


class SocialNetworksLink(BaseModel):
    instagram_url = models.URLField()
    tiktok = models.URLField()
    youtube_url = models.URLField()
    telegram_url = models.URLField()
    facebook_url = models.URLField()


class Interview(BaseModel):
    video = models.FileField(upload_to='')
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    duration = models.DurationField()

    def __str__(self):
        return self.title


class MainPage(BaseModel):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='')
    rating = models.IntegerField()
    short_content = models.CharField(max_length=256)
    author = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Course(BaseModel):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to='')
    rating = models.IntegerField()

    short_content = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    price = models.IntegerField()

    def __str__(self):
        return self.title


class CommentsAboutCourse(BaseModel):
    overall_rating = models.IntegerField()
    overall_comments = models.IntegerField()

    title = models.CharField(max_length=128)
    image = models.ImageField()
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=256)
    count = models.IntegerField()

    total_duration = models.IntegerField()

    def __str__(self):
        return self.title


class RateCourse(BaseModel):
    rating = models.IntegerField(
        validators = [
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )

    text_field = models.TextField(blank=True,null=True)

class Blog(BaseModel):
    image = models.ImageField(upload_to='media/')

    content = models.TextField()
    author = models.CharField(max_length=128)

    viewers = models.IntegerField()

    def __str__(self):
        return self.author


    


