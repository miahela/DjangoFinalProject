from django.shortcuts import render
from .models import Post, UserCourseTimestamp
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About page"})

# def course(request):
#     return render(request, 'blog/singlepost.html')

def quiz(request):
    return render(request, 'blog/course_quiz.html')

# class PostListView(ListView):
#     model = Post
#     template_name = 'post/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     # ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    
    def user_viewed(self, timestamp):
        user = self.request.user
        if not user.is_authenticated:
            return
        upt, _ = UserCourseTimestamp.objects.get_or_create(
            user=user, product=self.get_object())
        upt.timestamp = timestamp
        upt.save()
        return upt.timestamp