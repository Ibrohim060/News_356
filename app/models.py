from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .managers import CategoryManager
from utils.views import group_queryset



class Category(models.Model):
    slug = models.SlugField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255,unique=True)
    custom = CategoryManager()
    objects = models.Manager()
    

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
            counter = 1
            original_slug = self.slug
            while Category.custom.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    @property
    def get_group_blogs(self):
        return group_queryset(3, self.blog_set.all())

    @property
    def get_group_blogs_2(self):
        return group_queryset(2, self.blog_set.all())

    @property
    def get_group_blogs_6(self):
        return group_queryset(6, self.blog_set.all())
    
    
    @property
    def get_group_blogs_3(self):
        return group_queryset(3, self.blog_set.all())


    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    class StatusEnum(models.TextChoices):
        PUBLISHED = 'published', 'Published'
        DRAFT = 'draft', 'Draft'
        
        

    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=255,choices=StatusEnum.choices,default=StatusEnum.DRAFT)

    like = models.ManyToManyField(User, related_name="like",blank=True)
    seen = models.ManyToManyField(User, related_name="seens",blank=True)

    tags = models.ManyToManyField(Tag)
    datetime = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return None

    def __str__(self):
        return f"{self.title}"



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE,null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"{self.blog} - {self.user} - {self.text[:20]}"









