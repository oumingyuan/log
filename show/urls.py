from django.urls import path

from show import views

app_name = 'show'
urlpatterns = (
    # 主页
    path('', views.home, name='index'),

    # 获取主机的ip 地址
    path('get_ip/', views.get_ip, name="get_ip"),

    # 激活跑批日志的程序
    path('submit/', views.submit, name="submit_log"),

    # 日志的邮件提醒接口，没有实现呢
    path("send_email/", views.send_email),

)
