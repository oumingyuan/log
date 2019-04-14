# -*- coding: utf-8 -*-


import requests


def get_initialize_session(login_data):
    log_session = requests.Session()

    url_login = "http://bpowls.northking.net:7070/pm/userLogin!login.do"

    # login_data = {'code': 'mingyuan.ou', 'password': '/yuan15555136971'}

    log_session.post(url_login, login_data)

    return log_session


def get_staff_id(log_session):
    response = log_session.get('http://bpowls.northking.net:7070/pm/userLogin!queryUserInfo.do')

    if response.json()['pojoMap']:

        staff_id = response.json()['pojoMap']['id']

        return staff_id

    else:

        print("这个人的id已经被回收")

        return ""
