from django.urls import path
from . import views
from .views import (
    PostDetailView,
)

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('course/', views.course, name='blog-course'),
    path('quiz/', views.quiz, name='blog-quiz'),
]
