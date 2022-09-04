# Generated by Django 4.0.5 on 2022-09-04 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_post_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCourseTimestamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, null=True, verbose_name='TTime Stamp')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timestamps', to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timestamps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]