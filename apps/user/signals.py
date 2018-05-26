#!/usr/bin/env python
# encoding: utf-8


from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from apps.utils.request import get_ip_address_from_request

User = get_user_model()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()


@receiver(user_logged_in)
def update_last_login_ip(user, request, **kwargs):
    """
    最近登录Ip 这里生成token也会当做登录
    """
    ip = get_ip_address_from_request(request)
    if ip:
        user.last_login_ip = ip
        user.save()

