from django.apps import AppConfig

class HomeConfig(AppConfig):  # Make sure this is "HomeConfig"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'  # Make sure this is 'home' and NOT 'polls'
