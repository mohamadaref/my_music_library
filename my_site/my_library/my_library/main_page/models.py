from django.db import models
import uuid
import random
class Fan(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField(blank=False)
    def __str__(self):
        return self.first_name+"+"+self.last_name+"/"+str(self.age)
    class Meta:
        managed = True


class Instrument(models.Model):
    instr = (
    ('v','violin'),
    ('a','acoustic'),
    )
    ins_name = models.CharField(max_length = 20, choices=instr, blank=True, help_text="kind of instrumend that is played")
    def __str__(self):
        return self.ins_name
    class Meta:
        managed = True


class Musician(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    instrument = models.ForeignKey(Instrument,on_delete = models.CASCADE , null = True , blank = True)
    score_star = models.IntegerField(default = 0)
    fan = models.ManyToManyField(Fan)
    def __str__(self):
        return self.first_name
    class Meta:
        managed = True

class Cover(models.Model):
    img_link = models.CharField(max_length = 200)
    def __str__(self):
        return self.img_link
    class Meta:
        managed = True

class Album(models.Model):
    musician = models.ForeignKey(Musician , on_delete = models.CASCADE)
    album_name = models.CharField(max_length = 100)
    release_date = models.DateField()
    cover = models.OneToOneField(Cover,on_delete=models.CASCADE,null = True,blank = True)
    album_score = models.IntegerField()
    def __str__(self):
        return self.album_name
    class Meta:
        managed = True


class Music(models.Model):
    music_name = models.CharField(max_length = 20 , blank = True)
    album = models.ForeignKey(Album,on_delete = models.CASCADE)
    musician = models.ForeignKey(Musician,on_delete = models.CASCADE)
    download_link = models.CharField(max_length = 200, null = True , blank = True , help_text = "the link that is used for download")
    def __str__(self):
        return self.music_name
    class Meta:
        managed = True
# Create your models here.
