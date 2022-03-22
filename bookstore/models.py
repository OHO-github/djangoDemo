from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(verbose_name='书名', max_length=50, default='', unique=True)
    pub = models.CharField(verbose_name='出版社', max_length=100, default='')
    prices = models.DecimalField(verbose_name='价格', max_digits=7, decimal_places=2)
    market_prices = models.DecimalField(verbose_name='零售价', max_digits=7, decimal_places=2, default=0.00)
    info = models.CharField(verbose_name='描述', max_length=100, default='')

    class Meta:
        db_table = 'book'
        verbose_name = '图书'
        verbose_name_plural = '图书'

    def __str__(self):
        return '%s_%s_%s_%s_%s' % (self.title, self.pub, self.prices, self.market_prices, self.info)


class Author(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=11, null=False)
    age = models.IntegerField(verbose_name='年龄', default=1)
    email = models.EmailField(verbose_name='邮件', null=True)

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = '作者'

    def __str__(self):
        return '%s_%s_%s' % (self.name, self.age, self.email)
