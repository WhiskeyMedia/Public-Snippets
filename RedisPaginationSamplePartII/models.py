from django.contrib.contenttypes.models import ContentType
from django.db import models

redis = path_to_your_redis_client
STORAGE_KEY = 'some_key_name'

class Article(models.Model):
    """
    Stores article data.
      > publish_date: Denotes when an instance of this class can be displayed to users.
                      If 'publish_date' is > now(), then only staff can view the instance.
    """
    publish_date = models.DateTimeField(auto_add_now=True)

class Review(models.Model):
    """
    Stores review data.
      > publish_date: Denotes when an instance of this class can be displayed to users.
                      If 'publish_date' is > now(), then only staff can view the instance.
    """
    publish_date = models.DateTimeField(auto_add_now=True)