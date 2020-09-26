from datetime import datetime
import pytz

from ScheduleItem import ScheduleItem

est_tz = pytz.timezone('US/Eastern')

class ScheduleManager:
    def __init__(self):        
        pass
    
    def load_schedule(self, schedule):
        self._schedule = schedule

    def current(self):
        rem = self.remainder()

        if len(rem) > 0:
            return rem[0]
        else:
            return None

    def next(self):
        rem = self.remainder()

        if len(rem) > 1:
            return rem[1]
        else:
            return None

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

    def process_request(self, command):
        response = ""

        if command == "dj":
            current = self.current()

            if current:
                response = "The current DJ is " + current.dj
            else:
                response = "No one is currently playing."
        elif command == "next":
            next = self.next()

            if next:
                response = "Next up is " + next.dj + "!"
            else:
                response = "This is the last DJ for the evening."
        else:
            response = "I'm sorry, I don't understand that command."
        return response