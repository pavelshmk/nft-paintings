from django.contrib import admin

from app.models import TokenData


@admin.register(TokenData)
class TokenDataAdmin(admin.ModelAdmin):
    list_display = 'title', 'id',
