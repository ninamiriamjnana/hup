from django.db import models

from zinnia.models import EntryAbstractClass

class EntryWithNewUrl(EntryAbstractClass):
    """Entry with '/blog/<id>/' URL"""

    @models.permalink
    def get_absolute_url(self):
        return ('zinnia_entry_detail', (),
                {'object_id': self.id})
