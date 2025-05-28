from django.db import models

# Create your models here.
class Author(models.Model):
    class RoleChoises(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        WRITER = 'writer', 'Writer'

    image = models.ImageField(upload_to='authors/images/')
    firts_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    role = models.CharField(max_length=255, choices=RoleChoises.choices,default=RoleChoises.ADMIN)
    about_author = models.TextField()

    @property
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return None
    
    def __str__(self):
        return f"{self.firts_name} {self.last_name}"
    






