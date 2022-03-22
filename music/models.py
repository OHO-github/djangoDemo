from django.db import models


# Create your models here.
class Music(models.Model):
    title = models.CharField(verbose_name='歌名', max_length=50)
    autuor = models.CharField(verbose_name='歌手', max_length=40)
    total_time = models.DecimalField(verbose_name='总时长', max_digits=4, decimal_places=2)
    issue_date = models.DateField(verbose_name='发行时间')
    album_name = models.CharField(verbose_name='专辑名称',  max_length=50)

    class Meta:
        db_table = 'music'
        verbose_name = '歌曲'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s_%s_%s_%s_%s' % (self.title, self.autuor, self.total_time, self.issue_date, self.album_name)


class Singer(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=11)
    sex = models.CharField(verbose_name='性别', max_length=11)
    age = models.IntegerField(verbose_name='年龄', default=1)
    nationality = models.CharField(verbose_name='国籍', max_length=11)
    date_of_birth = models.DateField(verbose_name='出生日期')

    class Meta:
        db_table = 'singer'
        verbose_name = '歌手'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s_%s_%s_%s_%s' % (self.name, self.sex, self.age, self.nationality, self.date_of_birth)
