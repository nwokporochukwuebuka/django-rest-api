from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
import requests
from django.core.mail import send_mail


@shared_task
def send_mail_content(recipient_email, mail_header, message_html, msg):
    recipient = ( recipient_email, )
    sender = "Chukwuebuka"

    send_mail(mail_header, msg, sender, recipient, html_message=message_html)

@shared_task
def test():
    time.sleep(5)
    print('Hello Async')

@shared_task()
def populate_dog():
    url = "https://dog.ceo/api/breeds/image/random"

    try:
        res = requests.get(url)
    except requests.ConnectionError as e:
        raise Exception("Failed Operation", e)

    if res.status_code in [200, 201]:

        # Create dog entry
        data = res.json()
        image_url = data.get("message", "")
        from event_controller.models import Dog
        Dog.objects.create(url=image_url)