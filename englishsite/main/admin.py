from django.contrib import admin
from .models import *


class DialogueAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Tiles)
admin.site.register(RBooks)
admin.site.register(Game)
admin.site.register(Dialogue, DialogueAdmin)
admin.site.register(Voc)
admin.site.register(Word)
