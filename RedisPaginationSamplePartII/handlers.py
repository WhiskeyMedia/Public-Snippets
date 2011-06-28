import time
from django.db.signals import post_save, post_delete

from models import STORAGE_KEY
from utils import build_value

def update_content_list(instance, sender, created, **signal_args):
    """
    Signal handler used add instances to the content list.
      > Note that we do NOT need to add an 'if created' check in this function.
        Since we're using a set instead of a list to store the data, we are
        guaranteed to have a unique entries in the content list.
      > We also want handle every post_save() event in the case that an object
        is updated and its publish_date is changed, so we can update its zscore
        (and thus its order in the set).
    """
    # Use the publish_date of the object as the 'score' and add the object to the set
    score = int(time.mktime(instance.publish_date.timetuple()))
    redis.zadd(STORAGE_KEY, build_value(instance), score)

def remove_from_content_list(instance, sender, **signal_args):
    " Signal handler used remove instances from the content list. "
    redis.zrem(STORAGE_KEY, build_value(instance))

# Set up post_save() signals to handle adding content to redis
post_save.connect(update_content_list, sender=Review)
post_save.connect(update_content_list, sender=Article)

# Set up post_delete() signals to handle removing content to redis
post_delete.connect(remove_from_content_list, sender=Review)
post_delete.connect(remove_from_content_list, sender=Article)