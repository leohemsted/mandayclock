from . import Patch
import pyexchange.exchange2010 as pyexchange2010


class PyExchangePatch(Patch):
    """
    Class to patch pyexchange
    """

    @classmethod
    def patch(cls):
        def __BaseExchangeCalendarEvent__repr__(self):
            return '<%s: %s (%s->%s)>' % (self.__class__.__name__, self.subject, self.start, self.end)

        pyexchange2010.BaseExchangeCalendarEvent.__repr__ = __BaseExchangeCalendarEvent__repr__