import json
import uuid
from datetime import timedelta
from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
import telebot

from users.models import EmailVerification, User
from users_service import settings


bot = telebot.TeleBot(settings.TELEGRAM_KEY, parse_mode=None)


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    code = uuid.uuid4()
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=code, user=user, expiration=expiration)
    record.send_verification_email()
    return None


@shared_task
def send_order_to_email(email, order):
    subject = f'Book Store - Order #{order}'
    message = f'Your order has been successfully created! The manager will contact you shortly.'
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
    return None


@shared_task
def send_order_to_telegram(order, first_name, last_name, phone, message, total_sum, total_quantity, extra_data):
    text = f'<b>New order - #{order[0]}</b>:\n' \
           f'Name: <b>{first_name[0]}</b>\n' \
           f'Last name: <b>{last_name[0]}</b>\n' \
           f'Phone: <b>{phone[0]}</b>\n' \
           f'Total sum: <b>{total_sum[0]}\n</b>' \
           f'Total quantity: <b>{total_quantity[0]}\n</b>' \
           f'Message: <b>{message[0] if message else "Empty"}</b>\n\n' \
           f'<b>Information about order</b>:\n'
    i = 1
    for data in json.loads(extra_data[0]):
        text += f'{i}. Book: {data["name"]},\n' \
                f'Quantity: {data["quantity"]},\n' \
                f'Sum: {data["sum"]}.\n\n'
        i += 1
    for manager in User.objects.filter(is_staff=True):
        bot.send_message(manager.telegram_id, text, parse_mode='html')
    return None
