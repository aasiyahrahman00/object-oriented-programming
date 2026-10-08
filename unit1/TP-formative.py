class Date:
    """Represents a year, month and day."""

def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    return date

def print_date(date):
    print(f"{date.year:04d}-{date.month:02d}-{date.day:02d}")

def date_to_tuple(date):
    return (date.year, date.month, date.day)

def is_after(d1, d2):
    """Checks wheather d1 is after d2"""
    return date_to_tuple(d1) > date_to_tuple(d2)

date1 = make_date(1933, 6, 22)
print_date(date1)

date2 = make_date(2019, 5, 2)
print_date(date2)

print(is_after(date2, date1))
print(is_after(date1, date2))


class Time:
    """Represents a time of day."""

def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds 

def is_after(t1, t2):
    """Check wether t1 is after t2."""
    return time_to_int(t1) > time_to_int(t2)

print(is_after(make_time(3,2, 1), make_time(3, 2, 0)))
print(is_after(make_time(3,2, 1), make_time(3, 2, 1)))
print(is_after(make_time(11, 12, 0), make_time(9, 40, 0)))