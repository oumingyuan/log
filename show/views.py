# -*- coding: utf-8 -*-
import datetime
import time

from django.http import HttpResponse
from django.shortcuts import render

from log.settings import EMAIL_FROM
from show.models import User
from show.service import company_log_main
import json
# 接收POST请求数据
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

from show.web import company_log_session, company_log_requests
from show.tool import server_tool


def home(request):
    return render(request, "show/index.html")


@csrf_exempt
def get_ip(request):
    print(request.GET)

    print("lala")
    # company_log_main.get_and_insert_log()
    return HttpResponse(server_tool.get_host_ip())


@csrf_exempt
def submit(request):
    print("进入 post")

    print(request.POST)

    if request.POST:
        print("lala")
        company_log_main.get_and_insert_log()
        return HttpResponse(json.dumps({'result': 'success'}))


@csrf_exempt
def send_email(request):
    email_title = '京北方日志邮件通知(测试邮件，收到给个回复)'
    # email_body = '测试邮件'
    # email = '709336535@qq.com'  # 对方的邮箱

    # 获取人员信息
    user_infos = User.objects.filter(status='1')

    for user_info in user_infos:
        login_data = {'code': user_info.code, 'password': user_info.password}

        session = company_log_session.get_initialize_session(login_data)
        staff_id = company_log_session.get_staff_id(session)

        result = company_log_requests.query_this_week(session, staff_id)

        log_status = result[0]['status']
        log_content = result[0]['content']

        if log_status == 100:
            email_body = "到目前为止【" + datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S") + "】，你的日志还没有提交，请注意登陆公司日志系统填写或者联系欧总【13336980260】修复软件。"

        else:
            email_body = "恭喜你提交了日志，日志内容是：" + log_content

            # 判断人员是否写日志

        if user_info.email != '0':
            email = user_info.email  # 收件人邮箱
            # time.sleep(600)
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

            if send_status:
                return HttpResponse("发送成功")
