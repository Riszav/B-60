from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def add(x, y):
    print(f"args {x} and {y}")
    sleep(10)
    return x + y


@shared_task
def send_otp(email, code):
    send_mail(
        "OTP code",
        f"your code {code}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    
@shared_task
def send_report():
    send_mail(
        "Report",
        "Что то ооооочень важное",
        settings.EMAIL_HOST_USER,
        ["riszav.01@gmail.com"],
        fail_silently=False,
    )