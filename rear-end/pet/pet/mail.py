import smtplib
import traceback
import threading
from email.mime.text import MIMEText
from email.header import Header

"""
    description: Send email using smtplib
    author: Tianze Wen & Fei Teng
    date: 2020-03-15
    lastUpdate: 2020-04-22
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
        # do not change these
        self.__to_address = to_address
        self.__mail_host = "smtp.qq.com"
        self.__mail_user = "dog.cat.hospital@foxmail.com"
        self.__mail_pass = "itsnkhdkfrpdeaje"
        self.__sender = 'dog.cat.hospital@foxmail.com'
        self.__receivers = []
        self.__receivers.append(self.__to_address)

    def send(self, message):
        try:
            smtp_obj = smtplib.SMTP_SSL(self.__mail_host, 465)
            smtp_obj.set_debuglevel(1)
            smtp_obj.login(self.__mail_user, self.__mail_pass)
            smtp_obj.sendmail(self.__sender, self.__receivers, message.as_string())
            smtp_obj.quit()
            print({"code": 200, "msg": "Mail sent successfully"})
        except smtplib.SMTPException:
            traceback.print_exc()
            print({"code": 400, "msg": "Mail delivery failed"})

    def send_register_mail(self):
        message = MIMEText('You have successfully registered Healing Paws Veterinary Hospital.', 'plain', 'utf-8')
        message['From'] = Header("Healing Paws Veterinary Hospital", 'utf-8')
        message['To'] = Header(self.__to_address, 'utf-8')
        subject = 'Healing Paws Veterinary Hospital Register'
        message['Subject'] = Header(subject, 'utf-8')

        t = threading.Thread(target=self.send, args=(message,), daemon=True)
        t.start()

    def send_appointment_mail(self):
        message = MIMEText('You have successfully made an appointment in Healing Paws Veterinary Hospital. We will deal with it as soon as possible.', 'plain', 'utf-8')
        message['From'] = Header("Healing Paws Veterinary Hospital", 'utf-8')
        message['To'] = Header(self.__to_address, 'utf-8')
        subject = 'Healing Paws Veterinary Hospital Appointment Made'
        message['Subject'] = Header(subject, 'utf-8')

        t = threading.Thread(target=self.send, args=(message,), daemon=True)
        t.start()

    def send_processing_mail(self):
        message = MIMEText('Your appointment is being processed by our doctor.', 'plain', 'utf-8')
        message['From'] = Header("Healing Paws Veterinary Hospital", 'utf-8')
        message['To'] = Header(self.__to_address, 'utf-8')
        subject = 'Healing Paws Veterinary Hospital Appointment Processing'
        message['Subject'] = Header(subject, 'utf-8')

        t = threading.Thread(target=self.send, args=(message,), daemon=True)
        t.start()

    def send_operation_mail(self):
        message = MIMEText('An operation date is settled or an operation is processed in Healing Paws Veterinary Hospital.', 'plain', 'utf-8')
        message['From'] = Header("Healing Paws Veterinary Hospital", 'utf-8')
        message['To'] = Header(self.__to_address, 'utf-8')
        subject = 'Healing Paws Veterinary Hospital Operation'
        message['Subject'] = Header(subject, 'utf-8')

        t = threading.Thread(target=self.send, args=(message,), daemon=True)
        t.start()

    def send_discharge_mail(self):
        message = MIMEText('Discharge date is settled in Healing Paws Veterinary Hospital.', 'plain', 'utf-8')
        message['From'] = Header("Healing Paws Veterinary Hospital", 'utf-8')
        message['To'] = Header(self.__to_address, 'utf-8')
        subject = 'Healing Paws Veterinary Hospital Discharge'
        message['Subject'] = Header(subject, 'utf-8')

        t = threading.Thread(target=self.send, args=(message,), daemon=True)
        t.start()

    def send_finish_mail(self):
        message = MIMEText('An appointment is completed in Healing Paws Veterinary Hospital.', 'plain', 'utf-8')
        message['From'] = Header("Healing Paws Veterinary Hospital", 'utf-8')
        message['To'] = Header(self.__to_address, 'utf-8')
        subject = 'Healing Paws Veterinary Hospital Appointment Completed'
        message['Subject'] = Header(subject, 'utf-8')

        t = threading.Thread(target=self.send, args=(message,), daemon=True)
        t.start()

    def send_cancel_mail(self):
        message = MIMEText('An appointment is canceled in Healing Paws Veterinary Hospital.', 'plain', 'utf-8')
        message['From'] = Header("Healing Paws Veterinary Hospital", 'utf-8')
        message['To'] = Header(self.__to_address, 'utf-8')
        subject = 'Healing Paws Veterinary Hospital Appointment Canceled'
        message['Subject'] = Header(subject, 'utf-8')

        t = threading.Thread(target=self.send, args=(message,), daemon=True)
        t.start()

    def send_discussion_mail(self):
        return {}