from pyzotero import zotero
from settings import ZotCred

print(ZotCred.library_id)
print(ZotCred.library_type)
print(ZotCred.api_key)

zot = zotero.Zotero(ZotCred.library_id, ZotCred.library_type, ZotCred.api_key)
print(zot)
items = zot.top(limit=5)

# we've retrieved the latest five top-level items in our library
# we can print each item's item type and ID
for item in items:
    print(item)
