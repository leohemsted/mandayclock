from abc import ABCMeta
from collections import namedtuple
from random import randint

class ExternalService(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def connect(self, username, password):
        pass

    def list_events(self):
        pass


Fact = namedtuple('Fact', ['fact', 'value', 'seconds_per_value'])

class FactService(object):
    __metaclass__ = ABCMeta

    def __init__(self, facts, number_of_attendees, elapsed_seconds):
        self._validate_facts(facts)

        self.number_of_attendees = number_of_attendees
        self.elapsed_seconds = elapsed_seconds
        self.facts = facts

    def _validate_facts(self, facts):
        if any(not isinstance(fact, Fact) for fact in facts): raise ValueError('Use the Fact class!')

    def get_facts(self, number, unique=True):
        if unique:
            return self._get_unique_facts(number)
        else:
            return [self.get_fact() for i in xrange(number)]

    def get_fact(self):
        chosen = self.facts[randint(0, len(self.facts)-1)]
        return chosen.fact.format(value=chosen.value,
                                  seconds_per_value=chosen.seconds_per_value,
                                  elapsed_seconds=self.elapsed_seconds,
                                  total_value=chosen.value/chosen.seconds_per_value*self.elapsed_seconds)

    def _get_unique_facts(self, number):
        facts = []
        while len(facts) < number:
            fact = self.get_fact()
            facts.append(fact) if fact not in facts else None
        return facts
