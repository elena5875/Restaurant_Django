from django.db import models

# Create your models here.
class Review(models.Model):
    email = models.EmailField()
    review_text = models.TextField()
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email  