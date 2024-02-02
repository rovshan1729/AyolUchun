from rest_framework import generics
from . import models
from . import serializers

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class SocialNetworkLinkListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.SocialNetworksLink.objects.all()
    serializer_class = serializers.SocialNetworkLinkSerializer

class SocialNetworkLinkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SocialNetworksLink.objects.all()
    serializer_class = serializers.SocialNetworkLinkSerializer

class InterviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Interview.objects.all()
    serializer_class = serializers.InterviewSerializer

class InterviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Interview.objects.all()
    serializer_class = serializers.InterviewSerializer

class MainPageListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.MainPage.objects.all()
    serializer_class = serializers.MainPageSerializer

class MainPageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MainPage.objects.all()
    serializer_class = serializers.MainPageSerializer

class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class CommentsAboutCourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.CommentsAboutCourse.objects.all()
    serializer_class = serializers.CommentsAboutCourseSerializer

class CommentsAboutCourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CommentsAboutCourse.objects.all()
    serializer_class = serializers.CommentsAboutCourseSerializer

class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer

class RateCourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.RateCourse.objects.all()
    serializer_class = serializers.RateCourseSerializer

class RateCourseRetrieveUpdateDestroyAPIView(generics.ListCreateAPIView):
    queryset = models.RateCourse.objects.all()
    serializer_class = serializers.RateCourseSerializer

class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

