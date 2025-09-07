from django.core.exceptions import ValidationError
from django.db import models

class Quote(models.Model):
    text = models.TextField(verbose_name="Цитата")
    source = models.CharField(max_length=100, verbose_name="Источник (фильм, книга)")
    weight = models.PositiveIntegerField(default=1, verbose_name="Вес (шанс показа)")
    likes = models.PositiveIntegerField(default=0, verbose_name="Лайки")
    dislikes = models.PositiveIntegerField(default=0, verbose_name="Дизлайки")
    view_count = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"
        unique_together = ('text',)  # ← запрещает дубликаты

    def clean(self):
        if self.pk is None:  # если это новая цитата
            count = Quote.objects.filter(source=self.source).count()
            if count >= 3:
                raise ValidationError(
                    f"У источника '{self.source}' уже есть 3 цитаты. Нельзя добавить больше."
                )
        super().clean()

    def __str__(self):
        return f"{self.text[:50]}... ({self.source})"
