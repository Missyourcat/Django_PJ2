from django.db import models


# Create your models here.
class BookType(models.Model):
    id = models.AutoField(primary_key=True)
    bookTypeName = models.CharField(max_length=20)

    class Meta:
        db_table = 't_bookType'
        verbose_name = '图书类别信息'

    def __str__(self):
        return self.bookTypeName


class BookInfo(models.Model):
    id = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=20, verbose_name='图书名称')
    price = models.FloatField()
    publishDate = models.DateField()
    bookType = models.ForeignKey(BookType, on_delete=models.Prefetch)

    class Meta:
        db_table = 't_book'
        verbose_name = '图书信息'


class AccountInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20)
    account = models.FloatField()

    class Meta:
        db_table = 't_account'
        verbose_name = '用户账户信息'
