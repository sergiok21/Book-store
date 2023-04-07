from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.utils.timezone import now

from users_service import settings


class User(AbstractUser):
    is_verified_email = models.BooleanField(default=False)
    telegram_id = models.CharField(max_length=256, null=True, blank=True)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def send_verification_email(self):
        link = f'http://127.0.0.1:8005/users/verification/{self.user.email}/{self.code}/'
        subject = f'Account Verification {self.user.username}'
        message = f'To verify your email account {self.user.email}, please follow this link {link}'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        return True if now() >= self.expiration else False

    def __str__(self):
        return f'Email verification for {self.user.email}'
