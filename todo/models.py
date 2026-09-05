from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Título",
        max_length=100,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    deadline = models.DateField(
        verbose_name="Data de entrega",
    )

    finished_at = models.DateField(
        verbose_name="Data de finalização",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["deadline"]

    def mark_as_completed(self):
        if self.finished_at is None:
            self.finished_at = timezone.localdate()
            self.save()
