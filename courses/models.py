from django.contrib.auth.models import User
from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinValueValidator)
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class VideoCourse(BaseModel):
    class Status(models.TextChoices):
        sold = "sold", "sotip olingan"
        not_sold = "not_sold", "sotib olinmagan"

    title = models.CharField(max_length=100)
    price = models.IntegerField()
    viewer = models.ForeignKey(User, on_delete=models.CASCADE)
    short_content = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ContactNumber(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.name


class VideoDetail(BaseModel):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to="videos/")

    title_for_content = models.CharField(max_length=100)
    content = models.TextField()

    facebook_url = models.URLField()
    telegram_url = models.URLField()
    copy_link_url = models.URLField()

    def __str__(self):
        return self.title


class Video(BaseModel):
    title = models.CharField(max_length=255)
    duration = models.DurationField()

    def __str__(self):
        return self.title


class Lesson(BaseModel):
    title = models.CharField(max_length=100)
    number_of_videos = models.IntegerField()
    videos = models.ManyToManyField(Video)
    total_duration = models.DurationField()

    def save(self, *args, **kwargs):
        self.total_duration = sum(
            (video.duration for video in self.videos.all()), default=0
        )
        super().save(*args, **kwargs)
    

    class StatusOfProgress(models.TextChoices):
        IN_PROG = "in_prog", "Jarayonda"
        NOT_PURCHASED = "np", "Sotib olinmagan"
        COMPLETED = "com", "Ko'rilgan"
        NOT_SEEN = "not_seen", "Ko'rilmagan"

    status = models.CharField(
        max_length=25,
        choices=StatusOfProgress.choices,
        default=StatusOfProgress.NOT_PURCHASED,
    )

    def __str__(self):
        return self.title


class CommentsAboutCourse(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/")
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )

    overall_rating = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )
    overall_comments = models.IntegerField()

    rated_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return self.title


class CourseDetail(BaseModel):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to="videos/")
    title_of_video = models.CharField(max_length=100)
    short_content = models.TextField()
    liked = models.BooleanField(default=False)


class AboutVideo(BaseModel):
    comments = models.IntegerField()
    number_of_views = models.IntegerField()
    number_of_likes = models.IntegerField()
    language = models.CharField(max_length=100)
    video_duration = models.DurationField()


class UsefulResources(BaseModel):
    tasklist = models.FileField(upload_to="")
    youtube_tutorial_url = models.URLField()
    image = models.ImageField(upload_to="media/")


class CauseOfComplaint(BaseModel):
    class Complaints(models.TextChoices):
        ONE = (
            "1",
            "No-o'rin savol/izoh"
        )
        TWO = (
            "2",
            "Insonning shaniga teguvchi gaplar",
        )
        THREE = (
            "3",
            "Boshqalarga nisbatan so'kish va haqorat qiluvchi leksika",
        )
        FOUR = (
            "4",
            "Terrorizmga da'vat",
        )
        FIVE = (
            "5",
            "Tushunarsiz va umuman kerak bo'lmagan izoh",
        )
        SIX = (
            "6",
            "Boshqa",
        )

    complaint_type = models.CharField(max_length=100, choices=Complaints.choices)
    other_description = models.TextField(blank=True, null=True)


class Payment(BaseModel):
    price = models.ForeignKey(VideoCourse, on_delete=models.CASCADE)

    class PaymentType(models.TextChoices):
        PAYME = (
            "payme",
            "Payme",
        )
        APELSIN = (
            "apelsin",
            "Apelsin",
        )
        CLICK = (
            "click",
            "CLICK",
        )
        UZCARD = (
            "uzcard",
            "UZCARD",
        )
        VISA = (
            "visa",
            "VISA",
        )
        MASTERCARD = (
            "mastercard",
            "mastercard",
        )

    payment_type = models.CharField(max_length=100, choices=PaymentType.choices)


class PaymentDetails(BaseModel):
    full_name = models.CharField(max_length=255)
    card_number = models.IntegerField(
        validators=[
            MaxLengthValidator(16, message="The field must not exceed 16 digits. ")
        ]
    )
    validity_period = models.IntegerField(
        validators=[
            MaxLengthValidator(4, message="The field must not exceed 16 digits. ")
        ]
    )
    CVV = models.IntegerField(
        validators=[
            MaxLengthValidator(3, message="The field must not exceed 16 digits. ")
        ]
    )


class CommentsAboutVideo(BaseModel):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="")
    comment = models.TextField()
    left_comment = models.DateTimeField(auto_now_add=True)

    my_comment = models.TextField()


class RateCourse(BaseModel):
    rate = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )
    comment_about_course = models.TextField()


class Notification(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/")

    received_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

            