from django.db import models, backend, connection, transaction
from django.conf import settings
from django.core.validators import integer_re
from django.db.models.query import QuerySet, GET_ITERATOR_CHUNK_SIZE 
import pysvn

class SvnQuerySet(QuerySet):
    '''subclasses QuerySet to fetch older revisions from svn'''
    def __init__(self, model=None, revision='head'):
        self._rev = revision
        super(SvnQuerySet, self).__init__(model=model)
        
    def iterator(self):
        '''wraps the original iterator and replaces versioned fields with the 
           apropriate data from the given revision'''
        for obj in super(SvnQuerySet, self).iterator():
            for field in obj._meta.fields:
                if hasattr(field, 'IS_VERSIONED') and field.IS_VERSIONED and hasattr(self, '_rev') and not self._rev == 'head':
                    c = pysvn.Client()
                    svnrev = pysvn.Revision(pysvn.opt_revision_kind.number, int(self._rev))
                    olddata = c.cat(settings.SVN_WC_PATH+field.svn_path+'%s.txt' % obj.id, revision = svnrev)
                    setattr(obj, field.attname, olddata)
            yield obj

    def _filter_or_exclude(self, mapper, *args, **kwargs):
        '''this method makes sure cloned QuerySets inherit the _rev attribute'''
        clone = super(SvnQuerySet, self)._filter_or_exclude(mapper, *args, **kwargs)
        clone._rev = self._rev
        return clone
    
class RevisionManager(models.Manager):
    '''use this as default manager to get access to old revisions
        example usage::
        
            >>> from example.models import Entry
            >>> Entry.objects.get(pk=1).text
            ...
            >>> Entry.objects.rev(15).get(pk=1).text
            ...
            
    '''
    def get_query_set(self, rev='head'):
        return SvnQuerySet(self.model, revision=rev)
        
    def rev(self, rev='head'):
        if integer_re.search(str(rev)):
            if rev < 0:
                print "not implemented"
                #TODO: fetch head minus x if rev is < 0
                #get head revision and substract rev
                #c = pysvn.Client()
                
        return self.get_query_set(rev)
        