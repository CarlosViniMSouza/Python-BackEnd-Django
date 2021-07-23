# Templates are a Django framework that allows us to perform operations on databases without
# having to code in SQL or use third-party software to do so.

# But to make use of this, it is necessary to have knowledge of Classes and Inheritance
# in Python to perform the modeling.

from django.db import models

# Create your models here.

class Feature:
    id: int
    name: str
    details: str
