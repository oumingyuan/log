#!/usr/bin/python
# -*- coding: utf-8 -*-


from ..tool import date_tool

'''
查询日志的操作
'''


def query_this_week(session, staff_id):
    query_url = 'http://bpowls.northking.net:7070/pm/proLogInput!queryByLogDate.do'

    log_record_date = date_tool.get_seven_date()

    week_data = {'staffId': staff_id, 'logRecordDate': log_record_date}

    r2 = session.post(query_url, week_data)

    page_list = r2.json()['pageList']

    return page_list


def submit(log_record_date, information, work_hours, session, staff_id):
    # log_contents = 'RD-16-0471-01@eq@' + information

    save_data = {
        'staffId': staff_id,
        'logRecordDate': log_record_date,
        'logContents': information,
        'workHours': work_hours}

    r3 = session.post('http://bpowls.northking.net:7070/pm/proLogInput!submitLog.do', save_data)


def save(log_record_date, information, work_hours, session, staff_id):
    # log_record_date = five_date.get_five_date()

    # log_contents = 'RD-16-0471-01@eq@' + information

    save_data = {
        'staffId': staff_id,
        'logRecordDate': log_record_date,
        'logContents': information,
        'workHours': work_hours}

    r3 = session.post('http://bpowls.northking.net:7070/pm/proLogInput!saveLog.do', save_data)
