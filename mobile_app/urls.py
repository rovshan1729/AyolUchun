from django.urls import path
from . import views

urlpatterns = [
    path('category/lc/', views.CategoryListCreateAPIView.as_view(), name='category-lc'),
    path('category/rud/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-rud'),
    path('social-network-link/lc/', views.SocialNetworkLinkListCreateAPIView.as_view(), name='social-network-lc'),
    path('social-network-link/rud/', views.SocialNetworkLinkRetrieveUpdateDestroyAPIView.as_view(), name='social-network-rud'),
    path('interview/lc/', views.InterviewListCreateAPIView.as_view(), name='interview-lc'),
    path('interview/rud/', views.InterviewRetrieveUpdateDestroy.as_view(), name='interview-rud'),
    path('main-page/lc/', views.MainPageListCreateAPIView.as_view(), name='main-page-lc'),
    path('main-page/rud/', views.MainPageRetrieveUpdateDestroyAPIView.as_view(), name='main-page-rud'),
    path('course/lc/', views.CourseListCreateAPIView.as_view(), name='course-lc'),
    path('course/rud/', views.CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-rud'),
    path('comments/about-course/lc/', views.CommentsAboutCourseListCreateAPIView.as_view(), name='comments-about-course-lc'),
    path('comments/about-course/rud/', views.CommentsAboutCourseRetrieveUpdateDestroyAPIView.as_view(), name='comments-about-course-rud'),
    path('lesson/lc/', views.LessonListCreateAPIView.as_view(), name='lesson-lc'),
    path('lesson/rud/', views.LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson-rud'),
    path('rate-course/lc/', views.RateCourseListCreateAPIView.as_view(), name='rate-course-lc'),
    path('rate-course/rud/', views.RateCourseRetrieveUpdateDestroyAPIView.as_view(), name='rate-course-rud'),
    path('blog/lc/', views.BlogListCreateAPIView.as_view(), name='blog-lc'),
    path('blog/rud/', views.BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog-rud'),
]
