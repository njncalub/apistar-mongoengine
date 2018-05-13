import mongoengine
from apistar import exceptions
from mongoengine.errors import ValidationError
from mongoengine.queryset import (
    DoesNotExist,
    MultipleObjectsReturned,
    QuerySet,
)

from apistar_mongoengine.pagination import ListFieldPagination, Pagination


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
    
    def first_or_404(self):
        """
        Same as get_or_404, but uses .first, not .get.
        """
        obj = self.first()
        if obj is None:
            raise exceptions.NotFound()
        
        return obj
    
    def paginate(self, page, per_page, **kwargs):
        """
        Paginate the QuerySet with a certain number of docs per page and
        return docs for a given page.
        """
        return Pagination(self, page, per_page)
    
    def paginate_field(self, field_name, doc_id, page, per_page, total=None):
        """
        Paginate items within a list field from one document in the QuerySet.
        """
        item = self.get(id=doc_id)
        count = getattr(item, field_name + "_count", '')
        total = total or count or len(getattr(item, field_name))
        return ListFieldPagination(self, doc_id, field_name, page, per_page,
                                   total=total)


class Document(mongoengine.Document):
    """
    Abstract Document with extra helpers in the queryset class.
    """
    
    meta = {'abstract': True, 'queryset_class': BaseQuerySet}
    
    def paginate_field(self, field_name, page, per_page, total=None):
        """
        Paginate items within a list field.
        """
        count = getattr(self, field_name + "_count", '')
        total = total or count or len(getattr(self, field_name))
        return ListFieldPagination(self.__class__.objects, self.pk, field_name,
                                   page, per_page, total=total)


class DynamicDocument(mongoengine.DynamicDocument):
    """
    Abstract Dynamic Document with extra helpers in the queryset class.
    """
    
    meta = {'abstract': True, 'queryset_class': BaseQuerySet}


class EmbeddedDocument(mongoengine.EmbeddedDocument):
    """
    Abstract Embedded Document with extra helpers in the queryset class.
    """
    
    meta = {'abstract': True, 'queryset_class': BaseQuerySet}
