#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta


# 2018-03-05@eq@8@end@2018-03-06@eq@8@end@2018-03-07@eq@8@end@2018-03-08@eq@8@end@2018-03-09@eq@8
# result = request_session.query_this_week()


def get_work_hours(result):
    work_hours = ''
    for element in result:
        date_string = element['logDate']

        # 加横杠 20180305》》2018-03-05

        date_new = date_string[0:4] + "-" + date_string[4:6] + "-" + date_string[6:8] + "@eq@8@end@"

        work_hours = work_hours + date_new

    return work_hours[:-5]


# 2018-03-05,2018-03-06,2018-03-07,2018-03-08,2018-03-09
# logRecordDate

def get_log_record_date(result):
    work_hours = ''
    for element in result:
        date_string = element['logDate']

        # 加横杠 20180305》》2018-03-05

        date_new = date_string[0:4] + "-" + date_string[4:6] + "-" + date_string[6:8] + ","

        work_hours = work_hours + date_new

    return work_hours[:-1]


'''
获取本周周一到现在的日期组成的字符串

'''


def get_monday_to_now():
    day_week = datetime.now().weekday()
    day_today = datetime.today()
    day = day_today
    while day_week != 0:
        day = day + timedelta(-1)
        day_week = day.weekday()

    # 获取周一

    # 获取一周的日期

    seven_date = ''
    seven_date = seven_date + day.strftime('%Y-%m-%d') + ','
    day = day + timedelta(+1)
    while day != day_today:
        seven_date = seven_date + day.strftime('%Y-%m-%d') + ','
        day = day + timedelta(+1)
    seven_date = seven_date + day.strftime('%Y-%m-%d') + ','
    return seven_date[:-1]


'''
获取上周周一到周末的日期组成的字符串

'''


def get_monday_to_now_last_week():
    day = datetime.today()
    day = day + timedelta(-7)
    day_week = day.weekday()

    while day_week != 0:
        day = day + timedelta(-1)
        day_week = day.weekday()

    # 获取周一

    # 获取一周的日期

    seven_date = ''
    for i in range(1, 8):
        seven_date = seven_date + day.strftime('%Y-%m-%d') + ','
        day = day + timedelta(+1)
    return seven_date[:-1]


'''

'''


def get_five_date():
    day_week = datetime.now().weekday()
    day = datetime.today()
    while day_week != 0:
        day = day + timedelta(-1)
        day_week = day.weekday()

    # 获取周一

    # 获取一周的日期

    seven_date = ''
    for i in range(1, 6):
        seven_date = seven_date + day.strftime('%Y-%m-%d') + ','
        day = day + timedelta(+1)
    return seven_date[:-1]


def get_seven_date():
    day_week = datetime.now().weekday()
    day = datetime.today()
    while day_week != 0:
        day = day + timedelta(-1)
        day_week = day.weekday()

    # 获取周一

    # 获取一周的日期

    seven_date = ''
    for i in range(1, 8):
        seven_date = seven_date + day.strftime('%Y-%m-%d') + ','
        day = day + timedelta(+1)
    return seven_date[:-1]


def get_monday_to_now_db():
    day_week = datetime.now().weekday()
    day = datetime.today()
    while day_week != 0:
        day = day + timedelta(-1)
        day_week = day.weekday()

    # 获取周一

    # 获取一周的日期

    seven_date = ''
    seven_date = seven_date + '\'' + day.strftime('%Y-%m-%d') + '\'' + ','
    day = day + timedelta(+1)
    while day != datetime.today():
        seven_date = seven_date + '\'' + day.strftime('%Y-%m-%d') + '\'' + ','
        day = day + timedelta(+1)
    seven_date = seven_date + '\'' + day.strftime('%Y-%m-%d') + '\'' + ','
    return seven_date[:-1]


def get_five_date_before():
    day = datetime.today()
    day = day + timedelta(-7)
    day_week = day.weekday()

    while day_week != 0:
        day = day + timedelta(-1)
        day_week = day.weekday()

    # 获取周一

    # 获取一周的日期

    seven_date = ''
    for i in range(1, 8):
        seven_date = seven_date + day.strftime('%Y-%m-%d') + ','
        day = day + timedelta(+1)
    return seven_date[:-1]


# 2018-01-08@eq@8@end@2018-01-09@eq@8@end@2018-01-10@eq@8@end@2018-01-11@eq@8@end@2018-01-12@eq@8
# 2018-01-08@eq@8@end@2018-01-09@eq@8@end@2018-01-10@eq@8@end@2018-01-11@eq@8@end@2018-01-12@eq@8
def get_work_hours_without():
    day_week = datetime.now().weekday()
    day = datetime.today()
    while day_week != 0:
        day = day + timedelta(-1)
        day_week = day.weekday()

    # 获取周一

    # 获取一周的日期

    seven_date = ''
    for i in range(1, 6):
        seven_date = seven_date + day.strftime('%Y-%m-%d') + '@eq@8@end@'
        day = day + timedelta(+1)
    return seven_date
