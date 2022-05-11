from django.db import models


# users prototype for tg bot
# class TelegramUser(models.Model):
#     user_id = models.IntegerField("Telegram id", primary_key=True)
#     username = models.CharField("Username", max_length=32, null=True, blank=True)
#     first_name = models.CharField("First name", max_length=256)
#     last_name = models.CharField("Second name", max_length=256, null=True, blank=True)
#     language_code = models.CharField("User lang", max_length=8, null=True, blank=True)
#
#     is_blocked_bot = models.BooleanField(default=False)
#     is_banned = models.BooleanField(default=False)
#
#     is_admin = models.BooleanField(default=False)
#     is_moderator = models.BooleanField(default=False)
#
#     created_at = models.DateTimeField(auto_now_add=True, db_index=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table = 'telegram_users'
#         ordering = ('-created_at',)
#         verbose_name = 'TG user'
#         verbose_name_plural = 'TG users'
#
#     def __str__(self):
#         return self.username if self.username else str(self.user_id)
#
#     @property
#     def deep_link(self):
#         return f't.me/{self.username}' if self.username else None
