from django.contrib.contenttypes.models import ContentType
from django.db import models

redis = path_to_your_redis_client
STORAGE_KEY = 'some_key_name'

class Article(models.Model):
    def save(self, *args):
        created = not self.id
        super(Article, self).save(*args)

        # Only add brand new articles to the object list (ignore updates)
        if created:
            redis.lpush(STORAGE_KEY, "%d:%d" % (ContentType.objects.get_for_model(self), self.id))

    def delete(self):
        # Remove the article from the object list before deleting
        redis.lrem(STORAGE_KEY, "%d:%d" % (ContentType.objects.get_for_model(self), self.id))
        super(Article, self).delete()


class Review(models.Model):
    def save(self, *args):
        created = not self.id
        super(Review, self).save(*args)

        # Only add brand new reviews to the list (ignore updates)
        if created:
            redis.lpush(STORAGE_KEY, "%d:%d" % (ContentType.objects.get_for_model(self), self.id))

    def delete(self):
        # Remove the review from the object list before deleting
        redis.lrem(STORAGE_KEY, "%d:%d" % (ContentType.objects.get_for_model(self), self.id))
        super(Review, self).delete()
