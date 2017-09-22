import datetime
from haystack import indexes
from .models import Oeuvre


class OeuvreIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    auteur = indexes.CharField(model_attr='auteur')

    def get_model(self):
        return Oeuvre

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
