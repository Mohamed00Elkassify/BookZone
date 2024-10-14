from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    pdf_link = models.URLField()
    cover_image = models.ImageField(upload_to='cover/')
    bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return self.title
