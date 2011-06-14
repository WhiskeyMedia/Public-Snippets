Here is a sample app that contains views, models and a utility file that will demonstrate how to wire everything up.

================
Models:
The models.py file defines an Article and Review model. Both models override the save() and delete() methods to handle the insertion and deletion of objects of those respective classes from the object list maintained in redis.

Views:
The views.py file contains three views. The 'articles' and 'reviews' views show  pagination using the Django paginator against querysets of a single model. The 'articles_and_reviews' view provides an example of how to paginate objects that span multiple content types using the redis object list that we implemented in the models.py file.

Utils:
The utils.py file contains two utility functions that do the heavy lifting.