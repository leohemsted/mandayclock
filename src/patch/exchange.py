from . import Patch
import pyexchange.exchange2010 as pyexchange2010


class PyExchangePatch(Patch):
    """
    Class to patch pyexchange
    """
    def __BaseExchangeCalendarEvent__repr__(self):
        return '<%s: %s (%s->%s)>' % (self.__class__.__name__, self.subject, self.start, self.end)

    @classmethod
    def patch(cls):
        pyexchange2010.BaseExchangeCalendarEvent.__repr__ = cls.__BaseExchangeCalendarEvent__repr__