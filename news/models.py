from django.db import models
from django.contrib.auth import get_user_model

from common.models import BaseModel


User = get_user_model()

class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    


class News(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    



class MediaFile(models.Model):
    FILE_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
    )

    file_type = models.CharField(max_length=50, choices=FILE_TYPE_CHOICES)
    file = models.FileField(upload_to='media/')
    news = models.ManyToManyField('News', related_name='media_files')

    def __str__(self):
        return f"{self.file_type} - {self.file.name}"


class Tag(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    news = models.ManyToManyField(News, related_name='tags')

    def __str__(self):
        return self.name
    


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.email} on {self.news.title}"