from django.urls import path

from login import views

app_name = 'login'
urlpatterns = (
    # 主页
    path('', views.home, name='index'),

    # 获取主机的ip 地址
    path('register/', views.register, name="register"),
    path('login/', views.log_in, name="log_in"),
    path('get_request_info/', views.get_request_info, name="get_request_info"),

    path('check_name/', views.check_name, name="check_name"),

)
