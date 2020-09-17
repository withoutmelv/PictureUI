from django.db import models

# Create your models here.
from django.contrib.auth.models import User

'''
 这里我们自定义的UserProfile模型有三个字段
 1，user 与User是1对1 的关系
 2，org 用户名
 3，telephone 电话
 4， mod_date：最后修改日期，系统自动生成
'''


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    # 模型类中设置:blank=True,表示代码中创建数据库记录时该字段可传空白(空串,空字符串)
    org = models.CharField('Organization', max_length=128, blank=True)
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    folder = models.CharField('', max_length=128, blank=True)
    portrait = models.TextField(default="data:image/jpeg;base64,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")

    class Meta:
        verbose_name = 'User profile'

    def __str__(self):
        # return self.user.__str__()
        return "{}".format(self.user.__str__())
