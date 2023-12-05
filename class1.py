# class1.py

from datetime import datetime, timedelta
from calendar import monthrange

class MyDateTime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            dt_obj = datetime.utcnow()
            year, month, day = dt_obj.year, dt_obj.month, dt_obj.day

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second


    @classmethod
    def from_iso8601(cls, iso_string):
        dt_obj = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S")
        return cls(dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour, dt_obj.minute, dt_obj.second)

    def to_iso8601(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}T{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def to_human_readable(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d} {self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    @property
    def date(self):
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"

    @property
    def time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    @classmethod
    def is_valid_date(cls, day, month, year):
        try:
            monthrange(year, month)
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    @classmethod
    def date_difference(cls, date1, date2, unit='days'):
        delta = date2 - date1
        if unit == 'days':
            return delta.days
        elif unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return (date2.year - date1.year) * 12 + date2.month - date1.month
        else:
            raise ValueError("Invalid unit. Use 'days', 'weeks', or 'months'.")

    @classmethod
    def create_from_string(cls, date_string):
        dt_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
        return cls(dt_obj.year, dt_obj.month, dt_obj.day, dt_obj.hour, dt_obj.minute, dt_obj.second)

    @staticmethod
    def format_iso8601(date):
        return date.strftime("%Y-%m-%dT%H:%M:%S")

    @staticmethod
    def format_human_readable(date):
        return date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def calculate_weekday(date):
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return days_of_week[date.weekday()]

# Add the main block for testing
# Add the main block for testing
if __name__ == "__main__":
    dt = MyDateTime(2023, 11, 28, 12, 30, 45)
    print(dt.to_iso8601())
    print(dt.to_human_readable())
    print(MyDateTime.is_valid_date(31, 12, 2023))  # True
    print(MyDateTime.date_difference(datetime(2023, 11, 28), datetime(2023, 12, 5), unit='days'))  # 7
    print(MyDateTime.create_from_string("2023-11-28T12:30:45").to_iso8601())  # 2023-11-28T12:30:45
    print(MyDateTime.format_iso8601(datetime.utcnow()))  # Current UTC time in ISO 8601 format
    print(MyDateTime.calculate_weekday(datetime.utcnow()))  # Current day of the week
