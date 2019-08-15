from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')

    org = models.CharField('Organizarion',max_length=128,blank=True)
    telephone = models.CharField('Telephone',max_length=50,blank=True)

    mod_date =models.DateTimeField('Last modifiled',auto_now=True)

    class Meta:
        verbose_name ='User Profile'
    def __str__(self):
        return self.user.__str__()


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title
