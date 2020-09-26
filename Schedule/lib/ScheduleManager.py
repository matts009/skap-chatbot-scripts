from datetime import datetime
import pytz

from ScheduleItem import ScheduleItem

est_tz = pytz.timezone('US/Eastern')

class ScheduleManager:
    def __init__(self, schedule):
        self._schedule = schedule        

    def current(self):
        rem = self.remainder()

        if len(rem) > 0:
            print "Currently playing: {0}".format(rem[0].dj)
            return rem[0]
        else:
            print "No one is currently playing."
            return None

    def next(self):
        rem = self.remainder()

        if len(rem) > 1:
            print "Next up: {0}".format(rem[1].dj)
        elif len(rem) == 1:
            print "This is the last DJ of the evening."
        else:
            print "No one is currently playing."

    def location(self):
        schedule_item = self.current()

        if schedule_item is not None:
            print "{0} joins us from {1}!".format(schedule_item.dj, schedule_item.location)

    def remainder(self):
        now = datetime.now(est_tz)
        return filter(lambda x: now <= x.end_ts, self._schedule)

    def print_schedule(self):
        for item in self._schedule:
            print '{0} {1} {2}'.format(item.start_ts, item.end_ts, item.dj)

    def current_time(self):
        est_dt = datetime.now(est_tz)
        print(est_dt)