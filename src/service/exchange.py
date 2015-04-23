from . import ExternalService
from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection
from pyexchange.exceptions import FailedExchangeException
from pytz import timezone
from datetime import datetime as datetime  # so you can datetime while you datetime
from datetime import timedelta

class ExchangeLoginError(Exception):
    pass

class ExchangeService(ExternalService):
    def __init__(self, domain, url, days=3):
        self._service = None
        self._calendar = None
        self._domain = domain
        self._url = url
        self._days = days
        self.events = []

    def connect(self, username, password):
        connection = ExchangeNTLMAuthConnection(url=self._url,
                                                username='%s\\%s' % (self._domain, username),
                                                password=password)
        self._service = Exchange2010Service(connection)
        self._calendar = self._service.calendar()

    def _get_events(self):
        current_time = datetime.now()
        try:
            events_container = self._calendar.list_events(start=timezone("GMT").localize(current_time),
                end=timezone("GMT").localize(current_time + timedelta(days=self._days)),
                details=True)
        except FailedExchangeException as ex:
            raise ExchangeLoginError(ex.message)
        return self._build_event_list([event for event in events_container.events if event.attendees > 1])

    def _build_event_list(self, events):
        # TODO: Make this not pass around stuff specific to the underlying library
        self.events = events
        return events

    def list_events(self):
        if self.events:
            return self.events
        else:
            return self._get_events()