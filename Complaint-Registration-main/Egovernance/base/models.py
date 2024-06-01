from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify

choice=(
     ('Traffic Violation', 'Traffic Violation'),
    ('Delayed Services', 'Delayed Services'),
    ('Service Quality', 'Service Quality'),
    ('Service Denial', 'Service Denial'),
    ('Missuse of Funds', 'Missuse of Funds'),
    ('Road and Transportatoin Issues', 'Road and Transportation Issues'),
    ('Healthcare Services', 'Healthcare Services'),
    ('Misconduct Allegations', 'Misconduct Allegations'),
    ('Abuse of Power', 'Abuse of Power'),
    ('Other', 'Other'),
)

# Create your models here.
class Complaint(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=False, default='')
    email=models.EmailField(default='')
    description = models.TextField()
    category = models.CharField(max_length=100,choices=choice)
    image = models.ImageField(upload_to='image/', blank=True,null=True)
    action_taken=models.BooleanField(default=False,null=True,blank=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"])
        ]
    def save(self, *args, **kwargs):
            if not self.slug:
                base_slug = slugify(self.name)
                unique_slug = base_slug
                count = 1
                while Complaint.objects.filter(slug=unique_slug).exists():
                    unique_slug = f"{base_slug}-{count}"
                    count += 1
                self.slug = unique_slug
            super().save(*args, **kwargs)
    def __str__(self):
        return self.name