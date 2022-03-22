from django.contrib import admin
from music.models import Music, Singer


# Register your models here.
class MusicManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'autuor', 'total_time', 'issue_date', 'album_name']


class SingerManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'age', 'nationality', 'date_of_birth']


admin.site.register(Music, MusicManager)
admin.site.register(Singer, SingerManager)
