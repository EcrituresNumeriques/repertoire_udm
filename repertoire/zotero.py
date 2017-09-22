from pyzotero import zotero
from .models import Oeuvre
from django.core.exceptions import ObjectDoesNotExist

from zotero_credentials import *

class MyZotero():
    def __init__(self):
        self.api_key = ZOT_api_key
        self.library_id = ZOT_library_id
        self.library_type = ZOT_library_type

        self.zot = zotero.Zotero(self.library_id, self.library_type, self.api_key)

    def get_top(self, number=5):
        return self.zot.top(limit=number)

    def get_all(self, limit=50, start=0):
        return self.zot.items(limit=limit, start=start)

    def create_from_zotero_top(self, number=5):
        start = 0
        while start >= 0:
            elements = self.get_all(start=start)

            if len(elements):
                start += 50
            else:
                start = -1

            for z in elements:
                if z['data'].get('itemType', '') == 'attachment' or z['data'].get('title', '') == '':
                    continue

                local_elem = Oeuvre(
                    id_zotero=z['data']['key'],
                    url=z['data'].get('url', ''),
                    titre=z['data'].get('title', ''),
                )
                authors = ''
                for i in z['data'].get('creators', ()):
                    firstName = i.get('firstName', '')
                    lastName = i.get('lastName', '')
                    if firstName:
                        authors += firstName + ' '
                    authors += lastName + ', '

                local_elem.auteur = authors
                print("operating on " + z['data']['key'])
                local_elem.save()
