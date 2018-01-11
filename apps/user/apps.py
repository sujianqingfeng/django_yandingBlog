from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'
    verbose_name = u'用户操作'

    def ready(self):
        import user.signals
