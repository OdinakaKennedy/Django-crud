from django.contrib import admin

class Post(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
