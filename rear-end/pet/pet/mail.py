import smtplib
import traceback
from email.mime.text import MIMEText
from email.header import Header

"""
    description: send email using smtplib
    author: Tianze Wen
    date: 2020-03-15
    usage: 
        from mail import MailSender
        mail_sender = MailSender("xxxxxx@xxxxxx.com")
        mail_sender.send_register_mail()
    return: 
        {"code": 200, "msg": "xxxx"}
        {"code": 400, "msg": "xxxx"}
"""

class MailSender:
    def __init__(self, to_address):
        self.__to_address = to_address
        self.__mail_host = "smtp.qq.com"
        self.__mail_user = "dog.cat.hospital@foxmail.com"
        self.__mail_pass = "itsnkhdkfrpdeaje"
        self.__sender = 'dog.cat.hospital@foxmail.com'
        self.__receivers = []
        self.__receivers.append(self.__to_address)

    def send_register_mail(self):
        message = MIMEText('You have successfully registered Dog&cat Hospital', 'plain', 'utf-8')
        message['From'] = Header("Dog&cat Hospital", 'utf-8')
        message['To'] = Header(self.__to_address, 'utf-8')

        subject = 'Dog&cat Hospital register'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtp_obj = smtplib.SMTP_SSL(self.__mail_host, 465)
            smtp_obj.set_debuglevel(1)
            smtp_obj.login(self.__mail_user, self.__mail_pass)
            smtp_obj.sendmail(self.__sender, self.__receivers, message.as_string())
            smtp_obj.quit()
            return {"code": 200, "msg": "Register mail sent successfully"}
        except smtplib.SMTPException:
            traceback.print_exc()
            return {"code": 400, "msg": "Fail to sent register mail"}
