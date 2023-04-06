import uuid
from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from users.models import EmailVerification, User


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    code = uuid.uuid4()
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=code, user=user, expiration=expiration)
    record.send_verification_email()
    return None
