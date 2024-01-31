from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(
    r"contact/number", views.ContactNumberViewSet, basename="contact-number"
)
router.register(r"video/detail", views.VideoDetailViewSet, basename="video-detail")
router.register(r"video", views.VideoViewSet, basename="video")
router.register(r"lesson", views.LessonViewSet, basename="lesson")
router.register(
    r"comments/about/course",
    views.CommentsAboutCourseViewSet,
    basename="comment-about-course",
)
router.register(r"course/detail", views.CourseDetailViewSet, basename="course-detail")
router.register(r"about/video", views.AboutVideoViewSet, basename="about-video")
router.register(
    r"useful-resources", views.UsefulResourcesViewSet, basename="useful-resources"
)
router.register(
    r"cause-of-complaint", views.CauseOfComplaintViewSet, basename="cause-of-complaint"
)
router.register(r"payment", views.PaymentViewSet, basename="payment")
router.register(
    r"payment/detail", views.PaymentDetailsViewSet, basename="payment-details"
)
router.register(
    r"comment/about/video",
    views.CommentsAboutVideoViewSet,
    basename="comment-about-video",
)
router.register(r"rate/courses", views.RateCourseViewSet, basename="rate-course")
router.register(r"notification", views.NotificationViewSet, basename="notification")

urlpatterns = router.urls
