from django.contrib import admin
from main_page.models import Fan,Instrument,Musician,Album,Music,Cover

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_filter = ('ins_name',)


@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    pass


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_filter = ('first_name' , 'last_name' , 'instrument')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_filter = ('musician','album_name' , 'release_date')

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_filter = ('music_name','album')

@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):
    pass
# Register your models here.
