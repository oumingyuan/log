# -*- coding: utf-8 -*-

from django.shortcuts import render


def hello(request):
    context = {'hello': '页面导航'}
    return render(request, 'hello.html', context)
