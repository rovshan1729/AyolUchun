from rest_framework import serializers

from . import models


class VideoCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoCourse
        fields = [
            "id",
            "title",
            "price",
            "viewer",
            "short_content",
            "created_at",
            "updated_at",
        ]


class ContactNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactNumber
        fields = [
            "id",
            "name",
            "email",
            "phone_number",
            "comment",
            "created_at",
            "updated_at",
        ]


class VideoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoDetail
        fields = [
            "id",
            "title",
            "video_file",
            "title_for_content",
            "content",
            "facebook_url",
            "telegram_url",
            "copy_link_url",
            "created_at",
            "updated_at",
        ]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = [
            "id",
            "title",
            "duration",
            "created_at",
            "updated_at",
        ]


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = [
            "id",
            "title",
            "number_of_videos",
            "videos",
            "total_duration",
            "status",
            "created_at",
            "updated_at",
        ]


class CommentsAboutCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentsAboutCourse
        fields = [
            "id",
            "title",
            "image",
            "rating",
            "overall_rating",
            "overall_comments",
            "rated_at",
            "comment",
            "created_at",
            "updated_at",
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDetail
        fields = [
            "id",
            "title",
            "video_file",
            "title_of_video",
            "short_content",
            "liked",
            "created_at",
            "updated_at",
        ]


class AboutVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutVideo
        fields = [
            "id",
            "comments",
            "number_of_views",
            "number_of_likes",
            "language",
            "video_duration",
            "created_at",
            "updated_at",
        ]


class UsefulResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsefulResources
        fields = [
            "id",
            "tasklist",
            "youtube_tutorial_url",
            "image",
            "created_at",
            "updated_at",
        ]


class CauseOfComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CauseOfComplaint
        fields = [
            "id",
            "complaint_type",
            "other_description",
            "created_at",
            "updated_at",
        ]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = [
            "id",
            "price",
            "payment_type",
            "created_at",
            "updated_at",
        ]


class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentDetails
        fields = [
            "id",
            "full_name",
            "card_number",
            "validity_period",
            "CVV",
            "created_at",
            "updated_at",
        ]


class CommentsAboutVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentsAboutVideo
        fields = [
            "id",
            "full_name",
            "image",
            "comment",
            "left_comment",
            "my_comment",
            "created_at",
            "updated_at",
        ]


class RateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RateCourse
        fields = [
            "id",
            "rate",
            "comment_about_course",
            "created_at",
            "updated_at",
        ]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = [
            "id",
            "title",
            "image",
            "received_time",
            "created_at",
            "updated_at",
        ]
