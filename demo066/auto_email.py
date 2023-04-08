"""
python自动发邮件
"""

import smtplib
from email.mime import multipart, text


def send_email():
    # 连接到SMTP服务器
    smt_p = smtplib.SMTP()
    smt_p.connect(host='smtp.qq.com', port=25)
    # 这是我的邮箱用户名和授权码   授权码auth_code需要在qq邮箱设置
    sender, auth_code = '****@qq.com', '*********'
    smt_p.login(sender, auth_code)

    # 发送给谁
    email_address = '0070072727@163.com'
    try:
        msg = multipart.MIMEMultipart()
        msg['From'] = "nil ***********@qq.com"
        msg['To'] = email_address
        msg['subject'] = '你好，我是yangzhang'

        email_content = "你好, 这是邮件的主题内容，是一封测试邮件"
        msg.attach(text.MIMEText(email_content, 'plain', 'utf-8'))

        smt_p.sendmail(sender, email_address, msg.as_string())
    except Exception as e:
        # 写入日志
        print(e)
    smt_p.quit()


send_email()