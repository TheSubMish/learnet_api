from django.core.mail import EmailMessage
import os

class Util:
    @staticmethod
    def send_mail(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.environ['EMAIL_HOST_USER'],
            to=[data['to']]
        )
        email.send()