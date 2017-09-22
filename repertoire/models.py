from django.db import models
import tagulous.models

# Create your models here.
class TagAuteur(tagulous.models.TagModel):
    class TagMeta:
        pass

class TagLang(tagulous.models.TagModel):
    class TagMeta:
        pass

class Oeuvre(models.Model):
    titre = models.CharField(max_length=200, null=True, blank=False)
    auteur = models.CharField(max_length=200, null=True, blank=True)
    #auteur = tagulous.models.TagField(to=TagAuteur)
    url = models.URLField(max_length=200, null=True, blank=True)
    lieu = models.CharField(max_length=200, null=True, blank=True)
    langue = tagulous.models.TagField(to=TagLang)
    id_zotero = models.CharField(max_length=200, db_index=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.titre + ' ' + self.id_zotero
