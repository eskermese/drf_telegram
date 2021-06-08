from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'message',
        'created',
    )
    search_fields = (
        'message',
    )