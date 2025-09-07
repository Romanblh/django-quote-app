from django.contrib import admin
from .models import Quote

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text_short', 'source', 'weight', 'likes', 'view_count')
    list_editable = ('weight',)
    search_fields = ('text', 'source')

    def text_short(self, obj):
        return obj.text[:40] + "..."
    text_short.short_description = "Цитата"
