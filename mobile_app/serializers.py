from rest_framework import serializers
from . import models 


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = [
            'id',
            'title',
            'total',
            'created_at',
            'updated_at',
        ]

class SocialNetworkLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialNetworksLink
        fields = [
            'id',
            'instagram_url',
            'tiktok',
            'youtube_url',
            'telegram_url',
            'facebook',
            'created_at',
            'updated_at',
        ]

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Interview
        fields = [
            'id',
            'video',
            'title',
            'author',
            'duration',
            'created_at',
            'updated_at',
        ]

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MainPage
        fields = [
            'id',
            'title',
            'image',
            'rating',
            'short_content',
            'author',
            'created_at',
            'updated_at',
        ]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = [
            'id',
            'title',
            'image',
            'rating',
            'short_content',
            'author',
            'price',
            'created_at',
            'updated_at',
        ]

class CommentsAboutCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentsAboutCourse
        fields = [
            'id',
            'overall_rating',
            'overall_comments',
            'title',
            'image',
            'rating',
            'comment',
            'created_at',
            'updated_at',
        ]

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = [
            'id',
            'title',
            'count',
            'total_duration',
            'created_at',
            'updated_at',
        ]

class RateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RateCourse
        fields = [
            'id',
            'rating',
            'text_field',
            'created_at',
            'updated_at',
        ]

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = [
            'id',
            'image',
            'content',
            'author',
            'viewers',
            'created_at',
            'updated_at',
        ]

