# test_datetime_impl.py

from class1  import MyDateTime
from datetime import datetime, timedelta
# import pytest

def test_to_iso8601():
    dt = MyDateTime(2023, 11, 28, 12, 30, 45)
    assert dt.to_iso8601() == "2023-11-28T12:30:45"

def test_to_human_readable():
    dt = MyDateTime(2023, 11, 28, 12, 30, 45)
    assert dt.to_human_readable() == "2023-11-28 12:30:45"

def test_from_iso8601():
    dt = MyDateTime.from_iso8601("2023-11-28T12:30:45")
    assert dt.year == 2023
    assert dt.month == 11
    assert dt.day == 28
    assert dt.hour == 12
    assert dt.minute == 30
    assert dt.second == 45

def test_is_valid_date():
    assert MyDateTime.is_valid_date(31, 12, 2023) is True
    assert MyDateTime.is_valid_date(29, 2, 2023) is False  # Leap year

def test_date_difference():
    date1 = datetime(2023, 11, 28)
    date2 = datetime(2023, 12, 5)
    assert MyDateTime.date_difference(date1, date2, unit='days') == 7
    assert MyDateTime.date_difference(date1, date2, unit='weeks') == 1

def test_create_from_string():
    dt = MyDateTime.create_from_string("2023-11-28T12:30:45")
    assert dt.year == 2023
    assert dt.month == 11
    assert dt.day == 28
    assert dt.hour == 12
    assert dt.minute == 30
    assert dt.second == 45

def test_format_iso8601():
    current_time = datetime.utcnow()
    assert MyDateTime.format_iso8601(current_time) == current_time.strftime("%Y-%m-%dT%H:%M:%S")

def test_format_human_readable():
    current_time = datetime.utcnow()
    assert MyDateTime.format_human_readable(current_time) == current_time.strftime("%Y-%m-%d %H:%M:%S")

def test_calculate_weekday():
    current_time = datetime.utcnow()
    assert MyDateTime.calculate_weekday(current_time) in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']