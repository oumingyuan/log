# -*- coding: utf-8 -*-

from django.db import models

import django.utils.timezone as timezone


# 日志使用者模型
class User(models.Model):
    code = models.CharField('登录名', max_length=100)
    password = models.CharField('密码', max_length=100)
    name = models.CharField('名称', max_length=100)
    log = models.TextField('日志内容', max_length=100)
    email = models.CharField('邮箱', max_length=100)
    status = models.CharField('状态', max_length=100)
    name_pinyin = models.CharField('拼音', max_length=100)

    # 页面展示的标题
    class Meta:
        # 末尾不加s
        verbose_name_plural = '日志内容'
        verbose_name = '日志内容'

    def __str__(self):
        return self.name


# 这个应该显示最后一次写日志的记录
class Record(models.Model):
    add_date = models.DateTimeField('保存日期', default=timezone.now)
    reporter = models.CharField('保存日期', max_length=100)
    status = models.CharField('保存日期', max_length=100)

    class Meta:
        # 末尾不加s
        verbose_name_plural = '跑批信息'
        verbose_name = '跑批信息'
