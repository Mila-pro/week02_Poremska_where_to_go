from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField()
    rating = models.FloatField()  # (1.0, 1.5, …, 5.0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.rating})"

    def stars(self):
        """Повертає HTML із зірками ⭐ + половинками ✨"""
        full = int(self.rating)
        half = 1 if self.rating - full >= 0.5 else 0
        empty = 5 - full - half
        return "⭐" * full + ("✨" if half else "") + "☆" * empty 