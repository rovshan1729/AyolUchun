from rest_framework import viewsets

from . import models, serializers


# CONTACT NUMBER
class ContactNumberViewSet(viewsets.ModelViewSet):
    queryset = models.ContactNumber.objects.all()
    serializer_class = serializers.ContactNumberSerializer


class VideoCourseViewSet(viewsets.ModelViewSet):
    queryset = models.VideoCourse.objects.all()
    serializer_class = serializers.VideoCourseSerializer


class VideoDetailViewSet(viewsets.ModelViewSet):
    queryset = models.VideoDetail.objects.all()
    serializer_class = serializers.VideoDetailSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = models.Video.objects.all()
    serializer_class = serializers.VideoSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = models.Lesson.objects.all()
    serializer_class = serializers.LessonSerializer


class CommentsAboutCourseViewSet(viewsets.ModelViewSet):
    queryset = models.CommentsAboutCourse.objects.all()
    serializer_class = serializers.CommentsAboutCourseSerializer


class CourseDetailViewSet(viewsets.ModelViewSet):
    queryset = models.CourseDetail.objects.all()
    serializer_class = serializers.CourseDetailSerializer


class AboutVideoViewSet(viewsets.ModelViewSet):
    queryset = models.AboutVideo.objects.all()
    serializer_class = serializers.AboutVideoSerializer


class UsefulResourcesViewSet(viewsets.ModelViewSet):
    queryset = models.UsefulResources.objects.all()
    serializer_class = serializers.UsefulResourcesSerializer


class CauseOfComplaintViewSet(viewsets.ModelViewSet):
    queryset = models.CauseOfComplaint.objects.all()
    serializer_class = serializers.CauseOfComplaintSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer


class PaymentDetailsViewSet(viewsets.ModelViewSet):
    queryset = models.PaymentDetails.objects.all()
    serializer_class = serializers.PaymentDetailsSerializer


class CommentsAboutVideoViewSet(viewsets.ModelViewSet):
    queryset = models.CommentsAboutVideo.objects.all()
    serializer_class = serializers.CommentsAboutVideoSerializer


class RateCourseViewSet(viewsets.ModelViewSet):
    queryset = models.RateCourse.objects.all()
    serializer_class = serializers.RateCourseSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer
