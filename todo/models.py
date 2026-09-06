from django.core.exceptions import ValidationError
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

    def clean(self):
        super().clean()

        title = (self.title or "").strip()

        if not title:
            raise ValidationError({
                "title": "O título não pode conter apenas espaços."
            })

        self.title = title


        if self.deadline is None:
            return

        today = timezone.localdate()

        if self.deadline < today:
            if self.pk:
                original_deadline = type(self).objects.get(
                    pk=self.pk
                ).deadline

                if self.deadline == original_deadline:
                    return

            raise ValidationError({
                "deadline": "A data de entrega não pode ser no passado."
            })   

    def mark_as_completed(self):
        if self.finished_at is None:
            self.finished_at = timezone.localdate()
            self.save(update_fields=["finished_at"])
