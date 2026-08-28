from django.db import models
from autoslug import AutoSlugField
import uuid
# Create your models here.

class Poste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to="poste_image/")
    created_at = models.DateTimeField(auto_now_add=True)
    is_published=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    autor = models.EmailField()
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=True)
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.added_at}"

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.added_at}"