from datetime import datetime
import pytz

from ScheduleSheet import ScheduleSheet
from ScheduleItem import ScheduleItem

est_tz = pytz.timezone('US/Eastern')

class ScheduleManager:
    def __init__(self):
        self._sheet = ScheduleSheet()
        self._schedule = self._sheet.get_schedule()

    def current(self):
        rem = self.remainder()

        if len(rem) > 0:
            print "Currently playing: {0}".format(rem[0].dj)

    def next(self):
        rem = self.remainder()

        if len(rem) > 1:
            print "Next up: {0}".format(rem[1].dj)

    def remainder(self):
        now = datetime.now(est_tz)
        return filter(lambda x: now <= x.end_ts, self._schedule)

    def print_schedule(self):
        for item in self._schedule:
            print '{0} {1} {2}'.format(item.start_ts, item.end_ts, item.dj)

    def current_time(self):
        est_dt = datetime.now(est_tz)
        print(est_dt)