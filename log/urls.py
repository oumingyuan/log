"""log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
from django.urls import path, include
from log import views
from log.picture.controller import picture_download
import xadmin

# 之前是大括号，应为xadmin在windows上报错，所以改成中括号
urlpatterns = (

    # url(r'^$', views.hello),

    # path('admin/', admin.site.urls),

    # url(r'^xadmin/', xadmin.site.urls),

    # 跨域请求
    # url(r'^download_vue$', picture_download.download_vue),
    # url(r'^file_down$', picture_download.file_down),

    path('', views.hello),
    path('xadmin/', xadmin.site.urls),

    # 图片下载
    path('download_vue/', picture_download.download_vue),
    path('file_down/', picture_download.file_down),

    path('show/', include('show.urls')),
    path('login/', include('login.urls')),

)
