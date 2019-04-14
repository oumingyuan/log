#!/usr/bin/python
# -*- coding: utf-8 -*-


from show.tool import date_tool
from show.web import company_log_requests, company_log_session
from show.models import User, Record
from datetime import datetime
import logging

'''批量插入数据'''


def submit_log(my_login_data_new, weekday):
    print("#######  my_login_data_new:   " + str(my_login_data_new))

    login_data_variable = {'code': my_login_data_new.code, 'password': my_login_data_new.password}

    session = company_log_session.get_initialize_session(login_data_variable)
    staff_id = company_log_session.get_staff_id(session)

    print("#######  staff_id:   " + str(staff_id))

    if staff_id:  # 账户有效
        result = company_log_requests.query_this_week(session, staff_id)

        print("#######  result:   " + str(result))
        information_before = result[0]['projectCode']
        log_record_date = date_tool.get_log_record_date(result)

        information_after = my_login_data_new.log

        information = str(information_before) + '@eq@' + str(information_after)

        work_hours = date_tool.get_work_hours(result)

        if weekday == 6:  # 周末

            # 提交信息
            print("提交日志")
            logging.debug("开始提交日志内容")
            company_log_requests.submit(log_record_date, information, work_hours, session, staff_id)

        else:

            # 保存信息
            print("保存日志")
            logging.debug("开始保存日志内容")
            company_log_requests.save(log_record_date, information, work_hours, session, staff_id)

        # 记录日志文件
        page_list = company_log_requests.query_this_week(session, staff_id)
        logging.debug(page_list)
        reporter_name = page_list[0]["reporterName"]
        status_name = page_list[0]["status_Name"]

        record = Record(reporter=reporter_name, status=status_name)
        record.save()

        # company_log_dao.insert_log_status(reporter_name, status_name)
    else:

        print(login_data_variable)
        print("请删除无效的账户")

        # 数据库把这个账户设置为无效

        # my_login_data_new.update(status='0')

        User.objects.filter(id=my_login_data_new.id).update(status='0')


'''获取所有的用户信息'''


def get_and_insert_log():
    # 循环插入信息

    # 获取数据库信息
    # all_login_data_new = User.objects.all()

    all_login_data_new = User.objects.filter(status='1')

    # 打印时间
    day_today = datetime.today()

    # logging.basicConfig(filename='example.log', filemode="a", level=logging.DEBUG,
    #                     format='%(asctime)s - %(levelname)s - %(message)s')

    weekday = day_today.weekday()

    for login_data_new in all_login_data_new:
        submit_log(login_data_new, weekday)
