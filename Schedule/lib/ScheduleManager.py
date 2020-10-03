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
        #rem = self.remainder()
        now = datetime.now(est_tz)
        cur = filter(lambda x: now >= x.start_ts and now <= x.end_ts, self._schedule)

        if len(cur) > 0:
            return cur[0]
        else:
            return None

    def next(self):
        rem = self.remainder()

        if len(rem) > 1:
            return rem[1]
        else:
            return None

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
        response = None

        if command == "dj":
            current = self.current()

            if current:
                response = "Currently playing: {0} from {1}".format(current.dj, current.location)
            else:
                response = "No one is currently playing."
        elif command == "info":
            current = self.current()

            if current:
                resp_fmt = "{0} ({1}) playing {2} until {3}!"
                end_time = current.end_ts.strftime("%I:%M%p %Z").lstrip('0')
                response = resp_fmt.format(current.dj, current.location, current.genre, end_time)
        elif command == "next":
            next = self.next()

            if next:
                start_time = next.start_ts.strftime("%I:%M%p %Z").lstrip('0')
                response = "Next up: {0} ({1}) at {2}".format(next.dj, next.location, start_time)
            else:
                response = "This is the last artist for the evening."
        elif command == "more":
            current = self.current()

            if current:
                response = "Hear more of {0} at {1}".format(current.dj, current.website)
            else:
                response = ""
        elif command == "fb":
            response = "Visit us on Facebook! https://www.facebook.com/TheSlowKidsAtPlay"
        return response