from django.contrib.contenttypes.models import ContentType
from django.views.generic.simple import direct_to_template

from models import Article, Review, STORAGE_KEY, redis
from utils import paginate_list
RESULTS_PER_PAGE = 10

def articles_and_reviews(request, page=1):
    " This view returns a paginated list of both articles and review together. "
    object_list = paginate_list(
        page=page,
        results_per_page=RESULTS_PER_PAGE,
        storage_key=STORAGE_KEY
    )
    return direct_to_template(request, 'articles_and_reviews.html', {'objects':object_list})