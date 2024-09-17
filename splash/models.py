import logging
from django.db import models

logger = logging.getLogger(__name__)

logger.info("Defining User model")

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    marketing_consent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        logger.info(f"Saving user: {self.first_name} {self.last_name}")
        super().save(*args, **kwargs)
        logger.info(f"User saved with ID: {self.id}")