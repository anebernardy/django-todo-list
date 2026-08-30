from datetime import date

from django.db import models

class Todo(models.Model):
    title = models.CharField(verbose_name='Título', max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadLine = models.DateField(verbose_name='Data de entrega', null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ['deadLine']

    def mark_as_completed(self):
        if self.finished_at is None:
            self.finished_at = date.today()
            self.save()
