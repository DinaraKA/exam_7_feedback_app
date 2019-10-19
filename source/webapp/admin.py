from django.contrib import admin
from webapp.models import Poll, Choice, Answer


class PollAdmin(admin.ModelAdmin):
    list_display = ['pk', 'question', 'created_at']
    list_filter = ['created_at']
    list_display_links = ['pk', 'question']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Answer)
