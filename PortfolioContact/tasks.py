from celery import Celery, shared_task
from django.conf import settings
from django.core.mail import send_mail
from time import sleep

app = Celery('PortfolioContact', broker='redis://127.0.0.1:6379')

# import os

# os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "proj.settings"

@shared_task
def send_mail_to_user(name, email):
    status = send_mail(
        "Thanks for contacting",
        f"Hello {name}, \nI will get back to you shortly. \n\nAkhil Bhalerao.",
        settings.EMAIL_HOST_USER, [email], fail_silently=False
    )
    return status

@shared_task
def send_mail_to_admin(name, email, subject, desc):
    print(name, email, subject, desc)
    status = send_mail(
        subject,
        f"Sent by,\n    Name: {name} \n    Email: {email} \n\n{desc}",
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_TO_ADMIN],
        fail_silently=False
    )
    return status
    