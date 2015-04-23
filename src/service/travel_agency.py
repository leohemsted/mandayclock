import random

from . import FactService
from . import travel_times

class TravelAgency(FactService):
    def _validate_facts(self, facts):
        return True

    def get_fact(self):
        locations = travel_times.how_far_could_i_have_travelled(self.number_of_attendees, self.elapsed_seconds)
        return random.choice(locations)
