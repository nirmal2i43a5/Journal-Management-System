from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ReviewerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.reviewer'

    def ready(self):
        import apps.user.signals
        
        # migrate db before signals
        from apps.user.signals import populate_models
        post_migrate.connect(populate_models, sender=self)