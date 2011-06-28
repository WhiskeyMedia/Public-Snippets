from django.contrib.contenttypes.models import ContentType

redis = path_to_your_redis_client

def factory_object(ct_obj_string):
    """
    Utility function that takes a content_type:object_id
    string and returns a django object.
      @ct_obj_string => '1:22'  ('content_type_id:object_id')
    """
    # Split the string to get the content_type_id and the object_id
    ct_id, obj_id = ct_obj_string.split(':')
    return ContentType.objects.get_for_id(ct_id).models_class().objects.get(pk=obj_id)

def paginate_list(page=1, results_per_page=10, storage_key):
    """
    Utility function that will be used to paginate the
    object list based on the page you request and the results
    per page that you want back.
      @page => an optional int arg used to get the page in the
               pagination that the user wants.
      @results_per_page => an optional int arg used to tell the
               paginator how many results we want per page.
      @storage_key => required string that points to our object list
               in redis.
    """
    bottom = (page - 1) * results_per_page
    top = bottom + results_per_page - 1
    count = redis.llen()
    if top >= count:
        top = count - 1

    # Get the paginated object list out of redis
    # The list should look like: ["ct_id:obj_id", "ct_id:obj_id", "ct_id:obj_id"...]
    object_list = redis.zrrange(storage_key, bottom, top)

    # Factory and return each object
    return [factory_object(ct_obj_string) for ct_obj_string in object_list]

def build_value(instance):
    """
    Util method used to construct a string representation of an model object
    using the object's ContentType as well as its primary key (ct_id:obj_id).
    """
    return "%d:%d" % (ContentType.objects.get_for_model(instance).id, instance.id)