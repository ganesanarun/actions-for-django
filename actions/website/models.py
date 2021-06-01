from django.db.models import CharField, SlugField, Model


class Page(Model):
    name: CharField = CharField(max_length=50, unique=True)
    slug: SlugField = SlugField(unique=True)

