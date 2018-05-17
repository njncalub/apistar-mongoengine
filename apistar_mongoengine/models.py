import mongoengine
from apistar import exceptions
from apistar_mongoengine import types as as_me_types
from mongoengine.errors import ValidationError
from mongoengine.queryset import DoesNotExist, MultipleObjectsReturned, QuerySet

from apistar_mongoengine.pagination import Pagination


class BaseQuerySet(QuerySet):
    """
    Mongoengine's queryset extended with handy extras.
    """

    def get_or_404(self, *args, **kwargs):
        """
        Get a document and raise a 404 Not Found error if it doesn't exist.
        """
        try:
            return self.get(*args, **kwargs)
        except (MultipleObjectsReturned, DoesNotExist, ValidationError):
            # TODO: probably only DoesNotExist should raise a 404
            raise exceptions.NotFound()

    def first_or_404(self, *args, **kwargs):
        """
        Same as get_or_404, but uses .filter().first, not .get.
        """

        queryset = self.filter(*args, **kwargs)
        if not queryset:
            raise exceptions.NotFound()

        return queryset.first()

    def paginate(self, page, per_page, **kwargs):
        """
        Paginate the QuerySet with a certain number of docs per page and
        return docs for a given page.
        """
        return Pagination(self, page, per_page)


class Document(mongoengine.Document):
    """
    Abstract Document with extra helpers in the queryset class.
    """

    meta = {"abstract": True, "queryset_class": BaseQuerySet}


class DynamicDocument(mongoengine.DynamicDocument):
    """
    Abstract Dynamic Document with extra helpers in the queryset class.
    """

    meta = {"abstract": True, "queryset_class": BaseQuerySet}


class EmbeddedDocument(mongoengine.EmbeddedDocument):
    """
    Abstract Embedded Document with extra helpers in the queryset class.
    """

    meta = {"abstract": True, "queryset_class": BaseQuerySet}


class DocumentType(as_me_types.Type):
    pass
