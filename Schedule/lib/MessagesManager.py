from datetime import datetime, timedelta
import pytz

class MessagesManager:
    def __init__(self, sec_wait):
        self._sec_wait = sec_wait
        self._reset_timer()

    def _reset_timer(self):
        self._next_message_ts = datetime.now() + timedelta(seconds=self._sec_wait)
    
    def load_messages(self, messages):
        self._i = 0
        self._messages = messages

    def should_send_message(self):
        return datetime.now() > self._next_message_ts

    def get_next_message(self):
        self._reset_timer()

        if self._i == len(self._messages):
            self._i = 0
        
        i = self._i

        self._i += 1

        return self._messages[i]

    