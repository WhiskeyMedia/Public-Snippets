from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.views.generic.simple import direct_to_template

from models import Article, Review, STORAGE_KEY, redis
from utils import paginate_list
RESULTS_PER_PAGE = 10

def articles_and_reviews(request, page=1):
    " This view returns a paginated list of both articles and review together. "
    object_list = paginate_list(page=page, results_per_page=RESULTS_PER_PAGE, storage_key=STORAGE_KEY)
    return direct_to_template(request, 'articles_and_reviews.html', {'objects':object_list})

def articles(request, page=1):
    " This view returns a list paginated articles. "
    articles = Article.objects.all()
    paginator = Paginator(articles, RESULTS_PER_PAGE)
    page = paginator.page(page)
    return direct_to_template(request, 'articles.html', {'objects':page.object_list})

def reviews(request, page=1):
    " This view returns a list of pagianted reviews. "
    reviews = Review.objects.all()
    paginator = Paginator(reviews, RESULTS_PER_PAGE)
    page = paginator.page(page)
    return direct_to_template(request, 'reviews.html', {'objects':page.object_list})