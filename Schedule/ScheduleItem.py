class ScheduleItem:
    def __init__(self, sheet_row):
        self.date = sheet_row[0]
        self.start_time = sheet_row[1]
        self.end_time = sheet_row[2]
        self.dj = sheet_row[3]
        self.location = sheet_row[4]
        self.genre = sheet_row[5]

    def __str__(self):
        return "DJ " + self.dj 


