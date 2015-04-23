from patch.exchange import PyExchangePatch
PyExchangePatch.patch()

from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection
import config
from pytz import timezone
from datetime import datetime as datetime # so you can datetime while you datetime
from datetime import timedelta

connection = ExchangeNTLMAuthConnection(url=config.EXCHANGE_URL,
                                        username='%s\\%s' % (config.EXCHANGE_DOMAIN, config.EXCHANGE_USER),
                                        password=config.EXCHANGE_PASSWORD)

service = Exchange2010Service(connection)
calendar = service.calendar()

print dir(calendar)

current_time = datetime.now()


if __name__ == "__main__":
    events = calendar.list_events(start=timezone("US/Eastern").localize(current_time),
        end=timezone("US/Eastern").localize(current_time + timedelta(days=config.EXCHANGE_DAYS)),
        details=True)

    for event in events.events:
        attendees = len(event.attendees)
        if attendees > 1:
            # Ignore personal events
            print event.subject, attendees