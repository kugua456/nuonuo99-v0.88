#-*- coding:utf-8 -*-
from django.db import models
from django.conf import settings

from base.models import C_FlowerCategory, C_FlowerStyle, C_FlowerVariety


class StdProduct(models.Model):
    """每个产品, 推荐 4 个样图, 最少 1 个"""

    name = models.CharField(u'产品名称', max_length=255)
    desc = models.TextField(u'产品描述', max_length=255)
    price = models.DecimalField(u'单价', max_digits=8, decimal_places=2)

    photo1 = models.FileField(u'样图1', upload_to=settings.SERVICE_PATH)
    photo2 = models.FileField(u'样图2', upload_to=settings.SERVICE_PATH, blank=True)
    photo3 = models.FileField(u'样图3', upload_to=settings.SERVICE_PATH, blank=True)
    photo4 = models.FileField(u'样图4', upload_to=settings.SERVICE_PATH, blank=True)


    def __unicode__(self):
        return "%s-%s" % (self.name, self.price)

    class Meta:
        abstract = True


class WedFlower(StdProduct):
    """花艺产品"""
    category = models.ForeignKey(C_FlowerCategory, verbose_name=u'类型')
    style = models.ForeignKey(C_FlowerStyle, verbose_name=u'样式')
    scale = models.CharField(u'尺寸', max_length=32)
    color = models.CharField(u'颜色', max_length=32)
    items = models.ManyToManyField(C_FlowerVariety, through='FlowerItem', through_fields=('product', 'variety'))

    class Meta:
        verbose_name = u"花艺产品"
        verbose_name_plural = verbose_name


class FlowerItem(models.Model):
    product = models.ForeignKey(WedFlower, verbose_name=u'花艺产品')
    variety = models.ForeignKey(C_FlowerVariety, verbose_name=u'鲜花品种')
    amount = models.PositiveIntegerField(u'数量')

    def __unicode__(self):
        return '%s(%s)' % (self.variety, self.product)

    class Meta:
        verbose_name = u"花艺原料组成细节"
        verbose_name_plural = verbose_name
