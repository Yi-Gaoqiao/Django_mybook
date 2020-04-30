from django.db import models
from django.utils import timezone


class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=200)
    publisher = models.CharField('出版社', max_length=200, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)
    created_date = models.DateTimeField(default=timezone.now)
    end_reading_date = models.DateTimeField('読了日', blank=True, null=True)
    
    def end_reading(self):
        self.end_reading_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name



class Impression(models.Model):
    """
    感想
    related_name を使って以下のように読み出すことが可能。

    impressions = book.impressions.all().order_by('id')
    
    # 書籍の子供の、感想を読む
    
    """
    book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment

