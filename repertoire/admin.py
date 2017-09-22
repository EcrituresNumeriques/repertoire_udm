from django.contrib import admin
import tagulous.admin

from .models import *

# Register your models here.
admin.site.register(Oeuvre)

tagulous.admin.register(TagAuteur)
tagulous.admin.register(TagLang)
