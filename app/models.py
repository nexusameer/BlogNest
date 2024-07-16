from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils.text import slugify



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class BlogImages(models.Model):
    name = models.CharField(max_length=233)
    image = models.ImageField(null=True, blank=True, upload_to='blog_images')

    def __str__(self):
        return f'{self.image.name}'

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = models.CharField(max_length=100, blank=True, null=True)
    amazon_link = models.URLField(max_length=200, null=True, blank=True)
    images = models.ManyToManyField(BlogImages)
    

    class Meta:
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title