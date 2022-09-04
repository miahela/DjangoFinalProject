from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='default_course.jpg',upload_to='courses_pics')
    # date_posted = models.DateTimeField(default=timezone.now)
    date_last_access = models.DateTimeField
    duration = models.CharField(default='10hrs', max_length=20)

    author = models.CharField( max_length=100)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class UserCourseTimestamp(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="timestamps")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="timestamps")
    timestamp = models.DateTimeField("TTime Stamp", blank=True, null=True)

    # class Meta:
    #     db_table = 'timestamps'
