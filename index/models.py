from django.db import models

# Create your models here.

class Message(models.Model):
    """信息"""

    id = models.AutoField(verbose_name='序号', primary_key=True)
    name = models.CharField(verbose_name='名称', max_length=50)
    content = models.CharField(verbose_name='信息内容', max_length=200)
    addtime = models.DateField(verbose_name='反馈时间', auto_now=True)

    class Meta:
        verbose_name = '信息反馈表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

