# coding=utf-8
import smtplib
from email.mime.text import MIMEText


def send_email(msg_to):
    msg_from = 'oumingyuan@foxmail.com'  # 发送方邮箱
    password = 'tfbrbbfsewndbjhe'  # 填入发送方邮箱的授权码

    # msg_to = '709336535@qq.com'  # 收件人邮箱
    # msg_to = '1239532193@qq.com'  # 收件人邮箱

    subject = "京北方日志邮件通知"  # 邮件主题
    content = "你好，收到请别回信，这个是测试邮件。"

    msg = MIMEText(content)

    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号

    # s.ehlo()
    # s.starttls()

    s.login(msg_from, password)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")

    s.quit()
    s.close()
