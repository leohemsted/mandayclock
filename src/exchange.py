from patch.exchange import PyExchangePatch
PyExchangePatch.patch()

import config
from service.exchange import ExchangeService


if __name__ == "__main__":
    ex = ExchangeService(config.EXCHANGE_DOMAIN, config.EXCHANGE_URL)
    ex.connect(config.EXCHANGE_USER, config.EXCHANGE_PASSWORD)
    for event in ex.list_events():
        print "%s:" % event.subject
        print "\tDuration: %s from %s to %s" % (event.end - event.start, event.start, event.end)
        print "\tAttendees (%s): %s" % (len(event.attendees), ", ".join(person.name for person in event.attendees))